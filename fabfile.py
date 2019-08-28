import ujson as json
import re
from dataclasses import dataclass
from os import environ as env

import requests
from fabric import Connection
from fabric import task

REPO_NAME = 'schedule-API'
REPO_OWNER = 'thestd'
REPO_URL = f'https://github.com/{REPO_OWNER}/{REPO_NAME}'

APPS_ROOT = '~/applications'
PROJECT_ROOT = f'{APPS_ROOT}/{REPO_NAME}'


@dataclass
class WebhookData:
    action: str
    is_prerelease: bool
    is_draft: bool
    tag: str
    description: str

    @staticmethod
    def build(webhook_data):
        return WebhookData(webhook_data['action'],
                           webhook_data['release']['prerelease'],
                           webhook_data['release']['draft'],
                           webhook_data['release']['tag_name'],
                           webhook_data['release']['body'])


@task
def staging(ctx):
    ctx.user = env['SSH_USER']
    ctx.host = env['SSH_HOST']
    ctx.connect_kwargs.key_filename = env['SSH_KEY_FILENAME']


@task
def post_release_webhook(ctx):
    webhook_data = WebhookData.build(json.loads(env['POST_WEBHOOK_JSON']))
    if should_to_deploy(webhook_data):
        print('Run deploy process...')
        deploy(ctx, webhook_data.tag)
    else:
        print('Skip deploy process...')


@task
def deploy(ctx, tag):
    with remote_connection(ctx) as c:
        prepare(c)
        with c.cd(PROJECT_ROOT):
            deploy_process(c, tag)


def prepare(c):
    c.run(f'mkdir -p {APPS_ROOT}')
    with c.cd(APPS_ROOT):
        c.run(f'if [ ! -d {PROJECT_ROOT} ] ; then git clone {REPO_URL}; fi')


def deploy_process(c, tag):
    c.run('git fetch --all --tags --prune --prune-tags --progress')
    c.run(f'git checkout -f tags/{tag} -B release/{tag}')
    c.run(' &&'.join((
        'docker-compose down',
        'docker-compose up -d --build',
        'docker ps --format="table {{.Names}}\t{{.Ports}}\t{{.Status}}"'
    )))


def should_to_deploy(webhook: WebhookData) -> bool:
    latest_release_tag = get_latest_release_tag()
    skip_flag = re.search(r'(<!--)(\s+)?(skip-deploy)(\s+)?(-->)',
                          webhook.description, re.IGNORECASE)
    print('webhook = ', webhook,
          'latest_release_tag = ', latest_release_tag,
          'skip_flag = ', skip_flag)
    return ((not webhook.is_prerelease and not webhook.is_draft)
            and webhook.action in ('published', 'edited')
            and latest_release_tag == webhook.tag
            and not skip_flag)


def get_latest_release_tag():
    data = requests.get((f'https://api.github.com/repos/'
                         f'{REPO_OWNER}/{REPO_NAME}/releases/latest')).json()
    return data.get('tag_name')


def remote_connection(ctx):
    return Connection(host=ctx.host, user=ctx.user,
                      connect_kwargs=ctx.connect_kwargs)

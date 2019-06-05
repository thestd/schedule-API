from urllib.parse import urlencode
from tornado.options import options
from tornado import httpclient


def prepare_dates(**kwargs):

    date_from = kwargs.get('date_from', None)
    date_to = kwargs.get('date_to', None)

    date_from = (date_from.strftime('%d.%m.%Y').encode('cp1251')) if date_from else ''
    date_to = (date_to.strftime('%d.%m.%Y').encode('cp1251')) if date_to else ''

    return date_from, date_to


def prepare_post_data(**kwargs):

    sdate, edate = prepare_dates(**kwargs)

    group = kwargs.get('group', '')
    faculty = kwargs.get('faculty', 0)
    teacher = kwargs.get('teacher', '')

    post_data = {
        'faculty': faculty,
        'teacher': teacher.encode('cp1251'),
        'group': group.encode('cp1251'),
        'sdate': sdate,
        'edate': edate,
        'n': 700
    }

    return post_data


async def load_page(**kwargs):

    post_data = prepare_post_data(**kwargs)
    body = urlencode(post_data)
    async with httpclient.AsyncHTTPClient() as client:
        async with client.fetch(request=options.schedule_url,
                                method='POST',
                                headers=None,
                                body=body) as response:
            body = await response.body.decode('cp1251')
            return body


from urllib.parse import urlencode
from tornado.options import options
from tornado import httpclient
from json import loads, JSONDecodeError


def prepare_dates(**kwargs):

    date_from = kwargs.get('date_from', None)
    date_to = kwargs.get('date_to', None)

    date_from = (date_from.strftime('%d.%m.%Y').encode('cp1251')) if date_from else ''
    date_to = (date_to.strftime('%d.%m.%Y').encode('cp1251')) if date_to else ''

    return date_from, date_to


def prepare_post_data(**kwargs):

    sdate, edate = prepare_dates(**kwargs)

    group = kwargs.get('group', '')
    faculty = kwargs.get('faculty', '')
    teacher = kwargs.get('teacher', '')

    post_data = {
        'faculty': faculty.encode('cp1251'),
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

    response = await httpclient.AsyncHTTPClient().fetch(request=options.schedule_url,
                                                        method='POST',
                                                        headers=None,
                                                        body=body)

    return response.body.decode('cp1251')


async def load_teachers_or_groups(teachers=True, query='', faculty='0'):
    if teachers:
        api_code = options.teachers_api_code
    else:
        api_code = options.groups_api_code

    params = {
        'n': 701,
        'lev': api_code,
        'faculty': faculty,
        'query': query,
    }

    uri = options.ajax_url + urlencode(params)

    response = await httpclient.AsyncHTTPClient().fetch(request=uri,
                                                        headers=None,
                                                        method='GET')

    decoded_response = response.body.decode('cp1251')

    # if not teachers:
    # can't loads to json with non-escaped escape character
    decoded_response = decoded_response.replace('\\', '\\\\')

    # cause empty response is  {  "query":"",  "suggestions": ] }
    # wtf?
    try:
        return loads(decoded_response)['suggestions']
    except JSONDecodeError:
        return []

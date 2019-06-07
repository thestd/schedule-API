from tornado.options import options
from tornado.httpclient import HTTPRequest


def prepare_request(url=None, method='GET', body=None):
    if not url:
        url = options.schedule_url
    request = HTTPRequest(url=url,
                          method=method,
                          body=body)
    return request


def prepare_dates(**kwargs):

    date_from = kwargs.get('date_from', None)
    date_to = kwargs.get('date_to', None)

    date_from = (date_from.strftime('%d.%m.%Y').encode(options.base_encoding)) if date_from else ''
    date_to = (date_to.strftime('%d.%m.%Y').encode(options.base_encoding)) if date_to else ''

    return date_from, date_to


def prepare_post_data(**kwargs):

    # sdate, edate = prepare_dates(**kwargs)

    group = kwargs.get('group', '')
    faculty = kwargs.get('faculty', '')
    teacher = kwargs.get('teacher', '')
    sdate = kwargs.get('date_from', '')
    edate = kwargs.get('date_to', '')

    post_data = {
        'faculty': faculty,
        'teacher': teacher.encode(options.base_encoding),
        'group': group.encode(options.base_encoding),
        'sdate': sdate.encode(options.base_encoding),
        'edate': edate.encode(options.base_encoding),
        'n': 700
    }

    return post_data

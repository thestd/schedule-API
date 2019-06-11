from tornado.options import options
from tornado.httpclient import HTTPRequest


__all__ = ["prepare_request", "prepare_post_data", ]


def prepare_request(url=None, method='GET', body=None):
    # Todo: provide docstring
    if not url:
        url = options.schedule_url
    request = HTTPRequest(url=url,
                          method=method,
                          body=body,
                          connect_timeout=options.connection_timeout,
                          request_timeout=options.request_timeout)
    return request


def prepare_post_data(**kwargs):
    # Todo: provide docstring
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

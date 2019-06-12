from tornado.options import options
from tornado.httpclient import HTTPRequest


__all__ = ["prepare_request", "prepare_post_data", ]


def prepare_request(url=None, method='GET', body=None):
    """
    Args:
        url (str): Url for the request. If not specified - take default from options
        method (str): Request method. 'GET' by default
        body (str): Request body. None in most cases.

    Returns:
        request: object of HTTPRequest class
    """

    if not url:
        url = options.schedule_url
    request = HTTPRequest(url=url,
                          method=method,
                          body=body,
                          connect_timeout=options.connection_timeout,
                          request_timeout=options.request_timeout)
    return request


def prepare_post_data(**kwargs):
    """
    Args:
        kwargs

    Returns:
        post_data (dict): dict, prepared to use as body in POST request.

    """
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

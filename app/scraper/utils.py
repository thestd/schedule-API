from app import options
from tornado.httpclient import HTTPRequest


__all__ = ["prepare_request", "prepare_post_data", ]


def prepare_request(url=None, method='GET', body=None):
    """
    Args:
        url (str): Url for the request. If not specified - take default from options
        method (str): Request method. 'GET' by default
        body (str): Request body. None in most cases.

    Returns:
        HTTPRequest: request object
    """

    if not url:
        url = options.SCHEDULE_URL
    request = HTTPRequest(url=url,
                          method=method,
                          body=body,
                          connect_timeout=options.CONNECTION_TIMEOUT,
                          request_timeout=options.REQUEST_TIMEOUT)
    return request


def prepare_post_data(**kwargs):
    """
    Returns:
        dict: dict, prepared to use as body in POST request.

    """
    group = kwargs.get('group', '')
    faculty = kwargs.get('faculty', '')
    teacher = kwargs.get('teacher', '')
    sdate = kwargs.get('date_from', '')
    edate = kwargs.get('date_to', '')

    post_data = {
        'faculty': faculty,
        'teacher': teacher.encode(options.BASE_ENCODING),
        'group': group.encode(options.BASE_ENCODING),
        'sdate': sdate.encode(options.BASE_ENCODING),
        'edate': edate.encode(options.BASE_ENCODING),
        'n': 700
    }

    return post_data

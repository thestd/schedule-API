from tornado.options import options
from tornado.httpclient import HTTPRequest


__all__ = ["prepare_request", "prepare_post_data", ]


def prepare_request(url=None, method='GET', body=None):
    """
    :param url: Url for the request. If not specified - take default from options
    :type url: str
    :param method: Request method. 'GET' by default
    :type method: str
    :param body: Request body. None in most cases.
    :type body: str
    :return object of HTTPRequestW
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
    :param kwargs:
    :return dict, prepared to use as body in POST request.
    :rtype dict
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

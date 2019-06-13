from json import loads, JSONDecodeError

from urllib.parse import urlencode
from tornado.options import options
from tornado.httpclient import AsyncHTTPClient

from app.scraper.utils import prepare_post_data, prepare_request


__all__ = ["load_page", "load_schedule", "load_teachers_or_groups", ]


async def load_page(**kwargs):
    """
    Pass **kwargs to prepare_request() and send taken request with AsyncHTTPClient

    Returns:
        str: body of the HTTPClient.fetch() response

    """
    request = prepare_request(**kwargs)
    response = await AsyncHTTPClient().fetch(request=request)
    return response.body.decode(options.base_encoding)


async def load_schedule(**kwargs):
    """
    Wrapper around load_page()
    Pass **kwargs to prepare_post_data() to get body for POST request

    Returns:
        str: body of the HTTPClient.fetch() response

    """
    post_data = prepare_post_data(**kwargs)
    body = urlencode(post_data)

    return await load_page(method='POST', body=body)


async def load_teachers_or_groups(query='', faculty='0', teachers=False):
    """
    Send request to schedule url to get teachers or groups list

    Args:
        query (str):
        faculty(int, str): faculty code
        teachers(bool): False by default

    Returns:
        list: list of groups names if 'teachers' is False, else list of teachers names

    """
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

    url = options.ajax_url + urlencode(params)
    decoded_response = await load_page(url=url)

    # if not teachers:
    # can't loads to json with non-escaped escape character
    decoded_response = decoded_response.replace('\\', '\\\\')

    # cause empty response is  {  "query":"",  "suggestions": ] }
    # wtf?
    try:
        return loads(decoded_response)['suggestions']
    except JSONDecodeError:
        return []

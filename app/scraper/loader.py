from ujson import loads
from json import JSONDecodeError
from urllib.parse import urlencode

from app import options

from app.misc import session
from app.scraper.utils import prepare_post_data

__all__ = ["load_page", "load_schedule", "load_teachers_or_groups",
           "close_session"]


async def close_session(_):
    await session.close()


async def load_page(url=None, method='GET', body=None):
    """
    Send request to the schedule url

    Returns:
        str: decoded body of the response

    """
    if not url:
        url = options.SCHEDULE_URL
    async with session.request(url=url,
                               method=method,
                               data=body) as response:
        raw_response_body = await response.content.read()

        return raw_response_body.decode(options.BASE_ENCODING)


async def load_schedule(**kwargs):
    """
    Wrapper around load_page()
    Pass **kwargs to prepare_post_data() to get body for POST request

    Returns:
        str: decoded body of the response

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
        api_code = options.TEACHERS_API_CODE
    else:
        api_code = options.GROUPS_API_CODE

    params = {
        'n': 701,
        'lev': api_code,
        'faculty': faculty,
        'query': query,
    }

    url = options.AJAX_URL + urlencode(params)
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

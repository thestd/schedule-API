from urllib.parse import urlencode
from tornado.options import options
from tornado.httpclient import AsyncHTTPClient
from json import loads, JSONDecodeError
from app.scraper.utils import prepare_post_data, prepare_request


async def load_page(**kwargs):

    request = prepare_request(**kwargs)
    response = await AsyncHTTPClient().fetch(request=request)

    return response.body.decode(options.base_encoding)


async def load_schedule(**kwargs):

    post_data = prepare_post_data(**kwargs)
    body = urlencode(post_data)

    return await load_page(method='POST', body=body)


async def load_teachers_or_groups(query='', faculty='0', teachers=False):

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

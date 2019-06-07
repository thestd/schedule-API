from urllib.parse import urlencode
from tornado.options import options
from tornado import httpclient
from json import loads, JSONDecodeError
from app.scraper.utils import prepare_post_data


async def load_page(**kwargs):

    post_data = prepare_post_data(**kwargs)
    body = urlencode(post_data)

    response = await httpclient.AsyncHTTPClient().fetch(request=options.schedule_url,
                                                        method='POST',
                                                        headers=None,
                                                        body=body)

    return response.body.decode(options.base_encoding)


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

    decoded_response = response.body.decode(options.base_encoding)

    # if not teachers:
    # can't loads to json with non-escaped escape character
    decoded_response = decoded_response.replace('\\', '\\\\')

    # cause empty response is  {  "query":"",  "suggestions": ] }
    # wtf?
    try:
        return loads(decoded_response)['suggestions']
    except JSONDecodeError:
        return []

from aiohttp import web
import functools
from app.scraper.loader import load_page, load_teachers_or_groups, \
    load_schedule
from app.scraper.parser import parse_schedule, parse_faculties
from app.scraper.serializers import serialize_schedule, serialize_list
from app.options import CORS


def cors_headers(f):

    def _add_headers(response):
        for key, value in CORS.items():
            response.headers[key] = value
        return response

    @functools.wraps(f)
    async def new_f(*args):
        response = await f(*args)
        return _add_headers(response)
    return new_f


@cors_headers
async def schedule_handler(request):

    group = request.query.get('group', '')
    teacher = request.query.get('teacher', '')
    faculty = request.query.get('faculty', '0')
    date_from = request.query.get('date_from', '')
    date_to = request.query.get('date_to', '')
    # TODO: date validation
    query = group if group else teacher
    q_type = 'group' if group else 'teacher'

    body = await load_schedule(group=group,
                               teacher=teacher,
                               faculty=faculty,
                               date_from=date_from,
                               date_to=date_to)
    schedule = parse_schedule(body)
    schedule_json = serialize_schedule(query=query,
                                       q_type=q_type,
                                       schedule=schedule)

    return web.json_response(body=schedule_json, status=200)


@cors_headers
async def faculties_handler(request):
    body = await load_page()
    faculties_list = parse_faculties(body)
    faculties_json = serialize_list(faculties_list)
    return web.json_response(body=faculties_json, status=200)


@cors_headers
async def teachers_handler(request):

    query = request.query.get('query', '')
    faculty = request.query.get('faculty', '0')

    teachers_list = await load_teachers_or_groups(query=query,
                                                  faculty=faculty,
                                                  teachers=True)

    teachers_json = serialize_list(teachers_list)
    return web.json_response(body=teachers_json, status=200)


@cors_headers
async def groups_handler(request):
    query = request.query.get('query', '')

    groups_list = await load_teachers_or_groups(query=query)

    groups_json = serialize_list(groups_list)
    return web.json_response(body=groups_json, status=200)



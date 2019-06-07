from tornado.web import RequestHandler
from app.scraper.loader import (load_page,
                                load_teachers_or_groups)
from app.scraper.parser import (parse_schedule,
                                parse_faculties)
from app.scraper.serializers import (serialize_schedule,
                                     serialize_list)


class SceduleApiView(RequestHandler):

    async def get(self):

        group = self.get_query_argument('group')
        faculty = self.get_query_argument('faculty', '0')
        date_from = self.get_query_argument('date_from', '')
        date_to = self.get_query_argument('date_to', '')
        # TODO: date validation

        body = await load_page(group=group,
                               faculty=faculty,
                               date_from=date_from,
                               date_to=date_to
                               )
        schedule = parse_schedule(body)
        schedule_json = serialize_schedule(group=group,
                                           schedule=schedule)
        self.set_status(200)
        self.write(schedule_json)


class FacultiesApiView(RequestHandler):

    async def get(self):

        body = await load_page()
        faculties_list = parse_faculties(body)
        faculties_json = serialize_list(faculties_list)
        self.set_status(200)
        self.write(faculties_json)


class TeachersApiView(RequestHandler):

    async def get(self):

        query = self.get_query_argument('query', '', False)
        faculty = self.get_query_argument('faculty', '0', False)
        # TODO: validate faculty

        teachers_list = await load_teachers_or_groups(query=query,
                                                      faculty=faculty)

        teachers_json = serialize_list(teachers_list)
        self.set_status(200)
        self.write(teachers_json)


class GroupsApiView(RequestHandler):

    async def get(self):
        query = self.get_query_argument('query',  '', False)

        groups_list = await load_teachers_or_groups(teachers=False,
                                                    query=query)

        groups_json = serialize_list(groups_list)
        self.set_status(200)
        self.write(groups_json)

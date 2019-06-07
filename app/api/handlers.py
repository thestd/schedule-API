from tornado.web import RequestHandler
from app.scraper.loader import (load_page,
                                load_teachers_or_groups,
                                load_schedule)
from app.scraper.parser import (parse_schedule,
                                parse_faculties)
from app.scraper.serializers import (serialize_schedule,
                                     serialize_list)


class SceduleApiHandler(RequestHandler):

    async def prepare(self):

        group = self.get_query_argument('group')
        faculty = self.get_query_argument('faculty', '0')
        date_from = self.get_query_argument('date_from', '')
        date_to = self.get_query_argument('date_to', '')

        # TODO: date validation

        self.params = dict(group=group,
                           faculty=faculty,
                           date_from=date_from,
                           date_to=date_to
                           )

    async def get(self):

        body = await load_schedule(**self.params)
        schedule = parse_schedule(body)
        schedule_json = serialize_schedule(group=self.params['group'],
                                           schedule=schedule)
        self.set_status(200)
        self.write(schedule_json)


class FacultiesApiHandler(RequestHandler):

    async def get(self):

        body = await load_page()
        faculties_list = parse_faculties(body)
        faculties_json = serialize_list(faculties_list)
        self.set_status(200)
        self.write(faculties_json)


class TeachersApiHandler(RequestHandler):

    async def prepare(self):
        query = self.get_query_argument('query', '', False)
        faculty = self.get_query_argument('faculty', '0', False)

        # TODO: validate faculty

        self.params = dict(query=query,
                           faculty=faculty,
                           teachers=True)

    async def get(self):

        teachers_list = await load_teachers_or_groups(**self.params)

        teachers_json = serialize_list(teachers_list)
        self.set_status(200)
        self.write(teachers_json)


class GroupsApiHandler(RequestHandler):

    async def get(self):
        query = self.get_query_argument('query',  '', False)

        groups_list = await load_teachers_or_groups(query=query)

        groups_json = serialize_list(groups_list)
        self.set_status(200)
        self.write(groups_json)

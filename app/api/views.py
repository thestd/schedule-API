from tornado.web import RequestHandler
from app.scraper.loader import load_page
from app.scraper.parser import parse_schedule, serialize_schedule
from datetime import date


class SceduleApiView(RequestHandler):

    async def get(self):
        group = self.get_query_argument('group', 'КН-2')
        faculty = self.get_query_argument('group', '0')
        body = await load_page(group=group,
                               faculty=faculty,
                               date_from=date(day=25, month=4, year=2019),
                               date_to=date(day=2, month=5, year=2019)
                               )
        schedule = parse_body(body)
        schedule_json = serialize_schedule(group=group, schedule=schedule)
        self.set_status(200)
        self.write(schedule_json)


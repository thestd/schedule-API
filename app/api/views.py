from tornado.web import RequestHandler
from app.scraper.loader import load_page
from app.scraper.parser import parse_body
from datetime import date


class SceduleApiView(RequestHandler):

    async def get(self):
        group = self.get_query_argument('group', '')
        faculty = self.get_query_argument('group', '0')
        group = self.get_query_argument('group', '')
        body = await load_page(group='КН-2',
                                    date_from=date(day=3, month=6, year=2019),
                                    date_to=date(day=6, month=6, year=2019)
                                    )
        schedule_json = parse_body(body)
        self.set_status(200)
        self.write(schedule_json)


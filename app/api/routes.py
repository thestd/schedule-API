from app.api.handlers import schedule_handler, faculties_handler, \
                             teachers_handler, groups_handler
from aiohttp.web import get

__all__ = ["routes", ]


routes = [
    get(r"/api/schedule/?", schedule_handler),
    get(r"/api/faculties/?", faculties_handler),
    get(r"/api/groups/?", groups_handler),
    get(r"/api/teachers/?", teachers_handler),
]

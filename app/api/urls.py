from app.api.handlers import ScheduleApiHandler, FacultiesApiHandler, \
    TeachersApiHandler, GroupsApiHandler


__all__ = ["urls", ]


urls = [
    (r"/api/schedule/?", ScheduleApiHandler),
    (r"/api/faculties/?", FacultiesApiHandler),
    (r"/api/groups/?", GroupsApiHandler),
    (r"/api/teachers/?", TeachersApiHandler),
]

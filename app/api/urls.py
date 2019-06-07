from app.api.handlers import (SceduleApiHandler,
                              FacultiesApiHandler,
                              TeachersApiHandler,
                              GroupsApiHandler)

urls = [
    (r"/api/schedule/?", SceduleApiHandler),
    (r"/api/faculties/?", FacultiesApiHandler),
    (r"/api/groups/?", GroupsApiHandler),
    (r"/api/teachers/?", TeachersApiHandler),
]


from app.api.handlers import (SceduleApiHandler,
                              FacultiesApiHandler,
                              TeachersApiHandler,
                              GroupsApiHandler)

urls = [
    ("/api/schedule/", SceduleApiHandler),
    ("/api/faculties/", FacultiesApiHandler),
    ("/api/groups/", GroupsApiHandler),
    ("/api/teachers/", TeachersApiHandler),
]


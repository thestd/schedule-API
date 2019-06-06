from app.api.views import (SceduleApiView,
                           FacultiesApiView,
                           TeachersApiView,
                           GroupsApiView)

urls = [
    ("/api/schedule/", SceduleApiView),
    ("/api/faculties/", FacultiesApiView),
    ("/api/groups/", GroupsApiView),
    ("/api/teachers/", TeachersApiView),
]


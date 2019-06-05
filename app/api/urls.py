from app.api.views import SceduleApiView, FacultiesApiView

urls = [
    ("/api/schedule", SceduleApiView),
    ("/api/faculties", FacultiesApiView),
]

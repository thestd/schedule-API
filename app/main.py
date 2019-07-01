from aiohttp import web

from app.api.routes import routes
from app.options import APP_PORT


def _make_app(*args, **kwargs):
    """
    Defines main application `handlers` & `settings`

    :return Application:
    """

    app = web.Application(debug=True)
    app.add_routes(routes)
    return app


def run():
    web.run_app(_make_app(), port=APP_PORT)

from aiohttp import web

from app import options
from app.api.routes import routes


def _make_app(*args, **kwargs):
    """
    Defines main application `handlers` & `settings`

    :return Application:
    """

    app = web.Application(debug=options.DEBUG)
    app.router.add_routes(routes)
    return app


def run():
    web.run_app(_make_app(), port=options.APP_PORT)

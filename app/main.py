from aiohttp import web
import uvloop

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
    # Just trick to speed-up api-service
    uvloop.install()
    web.run_app(_make_app(), port=options.APP_PORT)

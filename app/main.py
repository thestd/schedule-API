from aiohttp import web

from app.api.routes import routes
from app.misc import app
from app.options import APP_PORT
from app.scraper.loader import close_session


def _make_app(*args, **kwargs):
    """
    Defines main application `handlers` & `settings`

    :return Application:
    """
    app.router.add_routes(routes)
    app.on_shutdown.append(close_session)
    return app


def run():
    web.run_app(_make_app(), port=APP_PORT)

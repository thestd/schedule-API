from aiohttp import web
import aioredis

from app.api.routes import routes
from app.misc import app
from app.options import APP_PORT
from app.scraper.loader import close_session


async def _make_app(*args, **kwargs):
    """
    Defines main application `handlers` & `settings`

    :return Application:
    """
    async def close_redis(a):
        a['redis'].close()

    app = web.Application(debug=options.DEBUG)
    app.router.add_routes(routes)
    app['redis'] = await aioredis.create_redis((options.REDIS_HOST, options.REDIS_PORT))
    app.on_shutdown.append(close_redis)
    app.on_shutdown.append(close_session)
    return app


def run():
    web.run_app(_make_app(), port=APP_PORT)

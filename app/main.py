import uvloop

uvloop.install()
from aiohttp import web
import aioredis
from app import options
from app.api.routes import routes
from aiohttp_swagger import setup_swagger


async def _make_app(*args, **kwargs):
    """
    Defines main application `handlers` & `settings`

    :return Application:
    """

    async def close_redis(a):
        a['redis'].close()

    app = web.Application(debug=options.DEBUG)
    app.router.add_routes(routes)
    if options.REDIS_URI:
        app['redis'] = await aioredis.create_redis_pool(options.REDIS_URI)
    else:
        app['redis'] = await aioredis.create_redis((options.REDIS_HOST,
                                                    options.REDIS_PORT))
    setup_swagger(app, swagger_from_file="swagger.yaml", ui_version=3)
    app.on_shutdown.append(close_redis)
    return app


def run():
    web.run_app(_make_app(), port=options.APP_PORT)

from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application

from .api.urls import urls as api_urls
from .options import load_conf


def _make_app():
    """
    Defines main application `handlers` & `settings`

    :return Application:
    """
    urls = [*api_urls]

    settings = {
        'handlers': urls,
        'debug': True
    }
    return Application(**settings)


def run():
    load_conf()
    app = _make_app()
    app.listen(options.app_port)

    IOLoop.instance().start()

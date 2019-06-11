from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application

from app.api.urls import urls as api_urls
from app.options import load_conf


def _make_app():
    # Todo: provide docstring
    urls = []
    urls.extend(api_urls)

    settings = {
        'handlers': urls,
        'debug': True
    }
    return Application(**settings)


if __name__ == '__main__':
    _make_app()
    load_conf()
    app = _make_app()
    app.listen(options.app_port)

    IOLoop.instance().start()

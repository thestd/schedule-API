from tornado.web import Application
from tornado.options import options
from app.api.urls import urls as api_urls
from options import load_conf


def make_app():

    urls = []
    urls.extend(api_urls)

    settings = {
        'handlers': urls,
        'debug': True
    }
    return Application(**settings)


load_conf()
app = make_app()
app.listen(options.app_port)



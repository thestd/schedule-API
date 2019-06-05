from tornado.ioloop import IOLoop
from app import app


if __name__ == '__main__':
    IOLoop.instance().start()

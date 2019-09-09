import aiohttp
import uvloop
from aiohttp import web

uvloop.install()
session = aiohttp.ClientSession(cookie_jar=aiohttp.DummyCookieJar())

app = web.Application(debug=True)

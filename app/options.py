import os

APP_PORT = int(os.getenv("PORT", 8085))

SECRET = "ABCDEFG!@#$%#"

DEBUG = False

SCHEDULE_URL = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?n=700"
AJAX_URL = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?"

TEACHERS_API_CODE = "141"
GROUPS_API_CODE = "142"

BASE_ENCODING = "cp1251"

CONNECTION_TIMEOUT = 1.5
REQUEST_TIMEOUT = 1.5

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_URI = os.getenv("REDIS_URI")

CACHE_PERIOD = 1
CORS = {
    'Access-Control-Allow-Origin': '*',
}

from tornado.options import options, define, parse_config_file


def load_conf(config_file=None):
    if config_file:
        parse_config_file(config_file)

    define("app_port", default=8085, help="Application port")
    define("secret", default="ABCDEFG!@#$%#", help="Secret key")
    define("schedule_url", default="http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?n=700", help="Why n=700?")
    define("ajax_url", default="http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?",
           help="Why n=701?")
    define("teachers_api_code", default="141", help="Why n is not 702?")
    define("groups_api_code", default="142", help="703")
    define("base_encoding", default="cp1251", help="encoding")

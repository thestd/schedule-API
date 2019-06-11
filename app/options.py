from tornado.options import define, parse_config_file


__all__ = ["load_conf", ]


def load_conf(config_file=None):
    # Todo: provide docstring
    if config_file:
        parse_config_file(config_file)

    define("app_port", default=8085, help="Application port")
    define("secret", default="ABCDEFG!@#$%#", help="Secret key")
    define("schedule_url",
           default="http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?n=700",
           help="Why n=700?")
    define("ajax_url", default="http://asu.pnu.edu.ua/cgi-bin/timetable.cgi?",
           help="Why n=701?")
    define("teachers_api_code", default="141", help="Why n is not 702?")
    define("groups_api_code", default="142", help="703")
    define("base_encoding", default="cp1251", help="encoding")
    define("connection_timeout", default=1.5, help="connection timeout")
    define("request_timeout", default=1.5, help="request timeout")

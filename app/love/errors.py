from . import love


@love.app_errorhandler(404)
def page_not_found(e):
    return "page not found"


@love.app_errorhandler(500)
def server_error(e):
    return "%s" % e

from . import main


@main.app_errorhandler(404)
def page_not_found():
    return "<h1>Page Not Found</h1>"


@main.app_errorhandler(500)
def internal_server_error():
    return "<h1>Internal Server Error</h1>"

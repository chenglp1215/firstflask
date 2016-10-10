from . import main


@main.route(r'/hello/', methods=['GET', 'POST'])
def hello():
    return "<p>hello</p>"

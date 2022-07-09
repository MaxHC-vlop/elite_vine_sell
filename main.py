from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


CREATE_YEAR = 1920


def get_year():
    now_year = datetime.now().year

    now_time = now_year - CREATE_YEAR

    return now_time


def make_template():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        old_wine = f'{get_year()}'
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

def main():
    make_template()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
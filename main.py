from pprint import pprint
import pandas
from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


CREATE_YEAR = 1920


def get_year():
    now_year = datetime.now().year
    now_time = now_year - CREATE_YEAR
    inf_name = now_time % 10
    inf_name2 = now_time % 100
    isll2 = 1
    iksl3 = (2, 3, 4)
    plop = (11, 12, 13, 14)
    if inf_name2 in plop:
        return f'{now_time} лет'
    elif inf_name == isll2:
        return f'{now_time} год'
    elif inf_name in iksl3:
        return f'{now_time} года'
    else:
        return f'{now_time} лет'


def new_name():
    excel_data_df = pandas.read_excel(
        'wine3.xlsx',
        keep_default_na=False,
        )
    wine_dict = excel_data_df.to_dict('records')
    vine_card = defaultdict(list)
    for vine in wine_dict:
        asdfa = vine['Категория']
        vine_card[asdfa].append(vine)

    sortedq = {key: value for key, value in sorted(vine_card.items())}

    return sortedq


def make_template():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    www = new_name()

    rendered_page = template.render(
        new_dict = new_name(),
        old_wine = get_year()
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    make_template()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

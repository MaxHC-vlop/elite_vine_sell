from collections import defaultdict

import pandas
from pprint import pprint


excel_data_df = pandas.read_excel('wine2.xlsx', keep_default_na=False)
wine_dict = excel_data_df.to_dict(orient='record')

vine_card = defaultdict(list)

for vine in wine_dict:
    asdfa = vine['Категория']
    vine_card[asdfa].append(vine)

pprint(vine_card)
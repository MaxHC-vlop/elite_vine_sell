from re import X
import pandas

excel_data_df = pandas.read_excel('wine.xlsx')
wine_dict = excel_data_df.to_dict()


qasdad = ('title', 'sort', 'price', 'image')
new_dict = []


for i in range(6):
    x = {
        'title': wine_dict['Название'][i],
        'sort': wine_dict['Сорт'][i],
        'price': wine_dict['Цена'][i],
        'image': wine_dict['Картинка'][i],
    }
    new_dict += [x]


print(new_dict)
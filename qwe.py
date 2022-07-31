from ast import match_case
from datetime import datetime




def get_year():
    now_year = datetime.now().year
    difference_year = now_year - CREATE_YEAR
    last_numbers_year = difference_year % 100
    last_number_year = difference_year % 10
    
    first_exception = 1
    second_exception = (range(2, 5))
    third_exception = (range(11, 21))

    if last_numbers_year in third_exception:
        return f'{difference_year} лет'

    else:
        if last_number_year is first_exception:
            return f'{difference_year} год'

        elif last_number_year in second_exception:
            return f'{difference_year} года'

        else:
            return f'{difference_year} лет'





while True:
    CREATE_YEAR = int(input())
    print(get_year())
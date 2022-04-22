from datetime import datetime


def data_hoje():
    (d, m, a) = (datetime.now().day, datetime.now().month, datetime.now().year)
    data = f'{d}/{m}/{a}'
    return data


print(f'{data_hoje()}')


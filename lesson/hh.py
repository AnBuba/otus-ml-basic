import datetime
from calendar import monthrange

start_date = datetime.date(2022, 6, 1)  # 2022, 6, 1 : stage_json_cross.users с июня
finish_date = datetime.date(2022, 10, 1)
delta = 5


print('CALC DATA IN NEW OBJECT VIA DBT')
while start_date < finish_date:
    current_year = start_date.year
    month = start_date.month
    days = monthrange(current_year, month)[1]

    if month == 6 or month == 7 or month == 8:
        start_date_2 = datetime.date(current_year, month, days)
        end_date = start_date + datetime.timedelta(days=days)
    else:
        start_date_2 = start_date
        end_date = start_date + datetime.timedelta(days=delta)


    print(start_date_2, end_date)

    if month == 6 or month == 7 or month == 8:
        start_date = start_date + datetime.timedelta(days=days)
    else:
        start_date = start_date + datetime.timedelta(days=delta)

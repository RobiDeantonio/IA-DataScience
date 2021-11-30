import datetime

my_time = datetime.datetime.now()
print(my_time)

my_time = datetime.date.today()
print(my_time)

my_str = my_time.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_time.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_time.strftime('It is the year %Y')
print(f'Formato random: {my_str}')
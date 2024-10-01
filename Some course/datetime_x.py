import datetime

utc_time = datetime.datetime.now(datetime.UTC)
current_time = datetime.datetime.now()

print(utc_time, current_time)
print(current_time.isoformat())
print(current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute)

some_datetime = datetime.datetime(year=2021, month=5, day=1, hour=12, minute=29)
print(some_datetime)

current_date = datetime.date.today()
print(current_date)

current_datetime_1 = datetime.datetime.now()
current_date_1 = current_datetime_1.date()

print(current_date_1)

current_date_2 = datetime.datetime.now()
day_ago = current_date_2 - datetime.timedelta(days=1)
print(day_ago)

print(current_time.strftime("%A, %d %B %Y"))

iso_format = "2023-08-07T20:15:30.384294"
my_datetime = datetime.datetime.fromisoformat(iso_format)
print(my_datetime, type(my_datetime))

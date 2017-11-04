import datetime, pprint

now = datetime.datetime.now()
print(now)

dt = datetime.datetime(2017, 10, 19, 16, 29, 0)
print((dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(f"Days:{delta.days}, seconds:{delta.seconds}")
print(now.strftime('%Y/%m/%d %H:%M:%S'))
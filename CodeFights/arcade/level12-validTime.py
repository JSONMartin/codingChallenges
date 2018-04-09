def validTime(time):
    hours, seconds = time.split(':')
    return 1 <= int(hours) <= 23 and 0 <= int(seconds) < 60


res = validTime("13:58")  # => True
print(res)
res = validTime("25:51")  # => False
print(res)
res = validTime("24:00")  # => False
print(res)

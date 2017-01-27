# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:
  format_duration(62)    # returns "1 minute and 2 seconds"
  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important.

Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
"""
# minute = 60
# hour = 3600
# day = 86400
# year = 31536000
def format_duration(duration):
    if duration <= 0: return "now"

    MINUTE, HOUR, DAY, YEAR = 60, 3600, 86400, 31536000
    years, days, hours, minutes, seconds = 0,0,0,0,0

    while duration >= YEAR:
        years += 1
        duration -= YEAR

    while duration >= DAY:
        days += 1
        duration -= DAY

    while duration >= HOUR:
        hours += 1
        duration -= HOUR

    while duration >= MINUTE:
        minutes += 1
        duration -= MINUTE

    seconds = duration

    results = [t for t in [(years, 'year' + ('s' if years > 1 else '')), (days, 'day' + ('s' if days > 1 else '')), (hours,'hour' + ('s' if hours > 1 else '')), (minutes, 'minute' + ('s' if minutes > 1 else '')), (seconds, 'second' + ('s' if seconds > 1 else ''))] if t[0] > 0]

    if len(results) > 1:
        return ", ".join([str(t[0]) + " " + t[1] for t in results[:-1]]) + " and " + (str(results[-1][0]) + " " + results[-1][1])
    else:
        return (str(results[-1][0]) + " " + results[-1][1])

#########
# TESTS
#########
format_duration(1)
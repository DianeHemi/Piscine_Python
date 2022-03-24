import datetime

t = (3, 30, 2019, 9, 25)
date = datetime.datetime(day=t[4], month=t[3], year=t[2], hour=t[0], minute=t[1])
print(date.strftime('%m/%d/%y %H:%M'))

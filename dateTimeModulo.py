import datetime

today=datetime.date.today()
print(today)

# How many days I alive ?
bDay=datetime.date(1999,9,3)
print('I lived '+ str((today-bDay).days) +' Days LOL ')

# Increase 10 days from now
increaseDate=datetime.timedelta(days=28)
print(today+increaseDate)

# Day of the date in int formate
print(today.day)
## month of the date in int format
print(today.month)
# Year of the date in int format
print(today.year)
# Weekend of the date in int format where 0==Mon,6==Sun
print(today.weekday())


todayDate=datetime.datetime.today()
timesNow=todayDate.time()
print(timesNow)

# Increase 10hours from now
increaseTime=datetime.timedelta(hours=20)
print(todayDate+increaseTime)

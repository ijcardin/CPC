import datetime
import calendar

list = [int(n) for n in input().split()]

inputDate = datetime.date(2009, list[1], list[0]) # YYYY-MM-DD
dayOfTheWeek = calendar.day_name[inputDate.weekday()]
print(dayOfTheWeek)










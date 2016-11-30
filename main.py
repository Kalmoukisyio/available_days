import datetime
from datetime import date,timedelta

today = datetime.date.today()

not_available_days = []
not_available_days.append(date(2016,11,29)) # sample not valid date 
available_days = [] 
commit_day = today
lead_time = 30

i = 1
j = 1
while i <= lead_time:
  current_day = commit_day + timedelta(days = j)
  if current_day.weekday() == 5 or current_day.weekday() == 6 or not_available_days.count(current_day) == 1:
    print("{} not valid".format(current_day))
  else:
    available_days.append(current_day)
    print("{}".format(current_day))
    i += 1
  j += 1

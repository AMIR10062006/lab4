from datetime import date,timedelta
Date = date.today()
print("today: ",Date)
Tomorrow = Date +\
    timedelta(days=1)
print("tomorrow: ",Tomorrow)
yesterday = Date -\
    timedelta(days=1)
print("yesterday: ",yesterday)


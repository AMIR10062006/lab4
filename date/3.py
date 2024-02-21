from datetime import datetime
Date =  datetime.today()
str = Date.isoformat()
print(str[0:-7])
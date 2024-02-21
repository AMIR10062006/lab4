from datetime import datetime as dt
date1 = dt(2002,12,12)
date2 = dt(2022,1,23)
diffinsec = abs((date2-date1).total_seconds())
print(diffinsec)


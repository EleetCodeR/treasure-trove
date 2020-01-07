from datetime import datetime
import time

dt = datetime(2018, 1, 1)  # yyy,mm,dd format, returns a datetime object.
dt = datetime.now()  # returns current datetime.

# Converting string value to Datetime.
# we must also provide directives for proper conversion.
# %Y = for 4 digit year, %m = 2 digit month, %d = 2 digit day. (many more such directives, can refer documentation.)
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")

# Converting a timestamp into Datetime.
dt = datetime.fromtimestamp(time.time())

print(f"Date:{dt.year}/{dt.month}/{dt.day}")

# converting a datetime object to string,
dt = dt.strftime("%Y/%m")
print(dt)

# Date Comparisons,
dt1 = datetime(2018, 1, 1)  # yyy,mm,dd format, returns a datetime object.
dt2 = datetime.now()  # returns current datetime.

print(dt2 > dt1)

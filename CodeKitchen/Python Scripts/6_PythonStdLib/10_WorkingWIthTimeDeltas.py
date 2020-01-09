from datetime import datetime, timedelta

# Timedeltas are mainly used for calculating timeduration.
# (they are the objects representing difference between two datetime instances)

dt1 = datetime(2018, 1, 1)  # yyy,mm,dd format, returns a datetime object.
dt2 = datetime.now()  # returns current datetime
duration = dt2-dt1  # THIS WILL RETURN OBJECT OTF TYPE TIMEDELTA.

print(duration)  # 737 days, 0:29:16.594092
print(type(duration))  # <class 'datetime.timedelta'>
print("days", duration.days)
# print("days", duration.month) # will throw error as timedelta class does not have month attribute.
# It is because of different variations in month and year.
print("seconds", duration.seconds)
print("total seconds", duration.total_seconds())

# we can alsoo add timedelta to datetime.
dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()
duration = dt2-dt1
print(duration)
    
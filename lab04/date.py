import datetime
#1
d = datetime.date.today() - datetime.timedelta(5)
print('Today:', datetime.date.today())
print('5 days before:', d)
print()

#2
yesterday = datetime.date.today() - datetime.timedelta(1)
tomorrow = datetime.date.today() + datetime.timedelta(1)
print('Yesterday:', yesterday)
print('Today:', datetime.date.today())
print('Tomorrow:', tomorrow)
print()

#3
dt = datetime.datetime.now().replace(microsecond = 0)
print(dt)
print()

#4
import datetime

def date_difference_in_seconds(date1, date2):
    date1_obj = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2_obj = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    difference_seconds = abs((date2_obj - date1_obj).total_seconds())
    
    return difference_seconds

date1 = "2005-10-02 10:00:00"
date2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference between the two dates in seconds:", difference_seconds)

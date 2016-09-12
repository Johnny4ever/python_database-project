import time
import calendar
ticks=time.time()
localtime=time.localtime(time.time())
print(ticks)
print(localtime)
print(time.asctime(localtime))
cal=calendar.month(2016,9)
print(cal)

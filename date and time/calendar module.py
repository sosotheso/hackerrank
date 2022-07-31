# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from datetime import datetime
lst = input().split()
dt = datetime.strptime(lst[2]+lst[0]+lst[1], "%Y%m%d").date()
print((calendar.day_name[dt.weekday()]).upper())
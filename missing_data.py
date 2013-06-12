import datetime as d
from data import *

def generate_dates(start_date, end_date):
    times = list()
    td = d.timedelta(hours=1)
    current_date = start_date
    while current_date <= end_date:
        times.append(current_date)
        current_date += td
    return times
###########################################

start_time = '2011-01-01 00:00:00'
end_time = '2012-12-31 23:00:00'

start = d.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
end = d.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
   
print start == end
     
times = generate_dates(start, end)

_, _, times_db = get_data(start_time, end_time, type='buy')

#print times
times_db = [x[0] for x in times_db]
#print times_db

missing = list(set(times).difference(set(times_db)))

print missing
print len(missing)


#list(set(b).difference(set(a))) 
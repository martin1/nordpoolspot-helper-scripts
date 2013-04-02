from data import *
import csv

def write_csv(start_date, end_date, curve_type='buy'):
    fmt = "%Y-%m-%d %H:%M:%S"
    prices, volumes, times = get_data(start_date, end_date, type=curve_type)
    #print times[0][0].month
    volumes_min = list()
    hours = list()
    
    '''for i in range(0, len(volumes)):
        volumes_min.append(min(volumes[i])) #find min volume for every curve
        hour = datetime.datetime.strftime(times[i], fmt)
        hours.append(times[i][0].hour)'''
        
    header = ["time", "min_volume", "month", "hour"]
    
    with open(curve_type+"_curve_data.csv", 'wb') as csvfile:
            wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            wr.writerow(header)
            for i in range(0, len(times)):
                time = times[i][0]
                wr.writerow([time, round(min(volumes[i]), 2), time.month, time.hour])
            csvfile.close()
    print "write_csv:done"
    
###############################
curve_type = 'sell'
start_date = '2011-01-01 00:00:00'
end_date = '2012-12-31 23:00:00'

write_csv
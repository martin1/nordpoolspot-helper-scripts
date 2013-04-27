from data import *
import csv
import matplotlib.pyplot as plt

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

def write_sys_prices(start_date, end_date):
    #get data
    buy_prices, buy_volumes, times = get_data(start_date, end_date, type='buy')
    #sell_prices, sell_volumes, _ = get_data(start_date, end_date, type='sell')
    sys_prices = list()
    
    for i in range(0, len(buy_prices)):
        #system_price = get_intersection_point(buy_volumes[i], buy_prices[i], sell_volumes[i], sell_prices[i])[1]#Only sys price is necessary
        #sys_prices.append(round(system_price, 3))
        '''print get_intersection_point(buy_volumes[i], buy_prices[i], sell_volumes[i], sell_prices[i])
        print buy_volumes[i]
        print buy_prices[i]
        print '--'
        print sell_volumes[i]
        print sell_prices[i]
        print sys_prices'''
        #plt.plot(buy_volumes[i], buy_prices[i], 'b-')
        #plt.plot(sell_volumes[i], sell_prices[i], 'r-')
    #plt.show()
    
    
    with open('sys_price_times_2012.csv', 'wb') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        #wr.writerow(["time", "system_price"])
        for i in range(0, len(times)):#sys_prices)):
            #print item
            wr.writerow([times[i][0]])#, sys_prices[i]])
        csvfile.close()
    print "write_sys_price:Done"
###############################
curve_type = 'sell'
start_date = '2012-01-01 00:00:00'
end_date = '2012-06-16 21:00:00'

write_sys_prices(start_date, end_date)

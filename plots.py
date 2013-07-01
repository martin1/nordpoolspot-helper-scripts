from data import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num, WeekdayLocator, MONDAY, MonthLocator,\
    DateFormatter, DayLocator
from matplotlib.pylab import figure, show
import csv

def plot_price_volume(buy_prices, buy_volumes, sell_prices, sell_volumes, show_intersections=False):
    
    intersect_x = None
    intersect_y = None
    
    for i in range(0, len(buy_prices)):
        
        x_buy = [r for r in buy_volumes[i]]
        y_buy = [r for r in buy_prices[i]]
        x_sell = [r for r in sell_volumes[i]]
        y_sell = [r for r in sell_prices[i]]
        f_buy = lambda x: interp(x, x_buy, y_buy)
        f_sell = lambda x: interp(x, x_sell, y_sell)
        
        if show_intersections == True:
   
            intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell, time=str(times[i]))
            plt.plot(intersect_x, intersect_y, 'go')
            
        plt.plot(x_buy, f_buy(x_buy), 'b-')#, linewidth=0.2, markersize=0.1)
        plt.plot(x_sell, f_sell(x_sell), 'r-')
        plt.annotate(str(intersect_x[0])+ ' | ' + str(intersect_y[0]), xy=(intersect_x, intersect_y),
                     xytext=(intersect_x-3000, intersect_y-100))
        #plt.plot(41500, 80.16, 'ro')
    
    plt.yticks(np.arange(-200, 2000, 100.0))
    plt.grid()
    plt.show()

def plot_time_price(times, prices):
    
    # every monday
    mondays   = WeekdayLocator(MONDAY)

    # every month
    months    = MonthLocator(range(1,13), bymonthday=1, interval=1)
    monthsFmt = DateFormatter("%b '%y")
    #days      = DayLocator(bymonthday=range(1,32))
    #daysFmt   = DateFormatter("%d.%m")
    times_num = [date2num(t) for t in times]
    
    fig = figure()
    ax = fig.add_subplot(111)
    ax.plot_date(times, prices, 'b-')
    
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_major_locator(months)
    #ax.xaxis.set_major_formatter(daysFmt)
    ax.xaxis.set_minor_locator(mondays)
    ax.autoscale_view()
    ax.grid(True)
    '''max'''
    ax.plot_date(times[prices.index(max(prices))], max(prices), 'ro')
    ax.annotate(str(times[prices.index(max(prices))])+'| '+ str(round(max(prices)[0], 2)), 
                xy=(times_num[prices.index(max(prices))], max(prices)),
                xytext=(times_num[prices.index(max(prices))], max(prices)))
    '''min'''
    ax.plot_date(times[prices.index(min(prices))], min(prices), 'ro')
    ax.annotate(str(times[prices.index(min(prices))])+'| '+ str(round(min(prices)[0], 2)), 
                xy=(times_num[prices.index(min(prices))], min(prices)),
                xytext=(times_num[prices.index(min(prices))], min(prices)))
    fig.autofmt_xdate()
    #plot csv times and prices
    
    #csv_times, csv_prices = get_times_prices_from_csv('sys_prices_real_2012.csv')
    #ax.plot_date(csv_times, csv_prices, 'r-')
    show()
    

def plot_time_volume(times, volumes):
    return plot_time_price(times, volumes)

def plot_time_curve_length():
    pass

def plot_time_max_volume():
    pass

def plot_time_min_volume():
    pass

def plot_time_min_max_volume():
    pass

def plot_time_volume_diff():
    pass
        
def get_times_prices_from_csv(csvfile):
    csv_times = list()
    csv_prices = list()
    
    data = csv.reader(open(csvfile, 'rb'), delimiter=',', quotechar='"')
    for item in data:
        csv_times.append(datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S"))
        csv_prices.append(item[1].replace(',', '.'))
    print csv_prices[0]
    return csv_times, csv_prices

'''Deprecated due to corrections applied to data in data module
def calculate_offset(buy_prices, buy_volumes, sell_prices, sell_volumes, actual_price):
    x_buy = [r for r in buy_volumes[0]]
    y_buy = [r for r in buy_prices[0]]
    x_sell = [r for r in sell_volumes[0]]
    y_sell = [r for r in sell_prices[0]]
    
    #check which way we should go along x-axis - positive or negative
    offset_step=1
    i=1
    
    _, original_intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell)
    
    x_sell_modified = [r+offset_step for r in x_sell]
    _, intersect_y = get_intersection_point(x_buy, y_buy, x_sell_modified, y_sell)
    if abs(actual_price - intersect_y) > abs(actual_price - original_intersect_y):
        offset_step = -1
    last_offset = min(abs(actual_price - intersect_y), abs(actual_price - original_intersect_y))
    
    #start shifting the supply curve in the appropriate direction
    while True:
        x_sell_modified = [r+(offset_step*i) for r in x_sell]
        _, intersect_y = get_intersection_point(x_buy, y_buy, x_sell_modified, y_sell)
        
        current_offset = abs(actual_price- intersect_y)
        if (current_offset < 0.2 or last_offset < current_offset):
            break
        else:
            last_offset = current_offset
        i+=1
    print offset_step*i
    return offset_step*i'''
    
########################################
start_date = '2011-08-07 00:00:00'
end_date = '2011-08-07 00:00:00'
#end_date = '2011-07-23 18:00:00'
#hour = '01:00:00'

buy_prices, buy_volumes, times = get_curve(start_date, end_date, type='buy', specified_hour = None)
sell_prices, sell_volumes, _ = get_curve(start_date, end_date, type='sell', specified_hour = None)
print sell_prices[0]
#print sell_prices[1]
print sell_volumes[0]
#print sell_volumes[1]
#print times
#plot_time_price(times, prices)
plot_price_volume(buy_prices, buy_volumes, sell_prices, sell_volumes, show_intersections=True)
'''csv_times, csv_prices = get_times_prices_from_csv("nps_sys_prices_real.csv")
volume_offsets = list()
for i in range(0, len(csv_times)):
    print str(csv_times[i])
    volume_offsets.append(calculate_offset(buy_prices, buy_volumes, sell_prices, sell_volumes, float(csv_prices[i])))
    print '---------'
 
with open('volume_offsets_2011.txt', 'w') as file:
    for item in volume_offsets:
        file.write(str(item)+'\n')
    file.close()'''
#plot_times_prices(csv_times, volume_offsets)
'''for i in range(0, len(buy_volumes)):
    plt.plot(buy_volumes[i], buy_prices[i], 'b-')
    plt.annotate(str(times[i][0].hour), 
                 xy=(buy_volumes[i][-1], buy_prices[i][-1]),
                 xytext=(buy_volumes[i][-1], buy_prices[i][-1] - 50))
plt.show()'''
#get_times_prices_from_csv('nps_sys_prices_real.csv')
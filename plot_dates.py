from data import *
from matplotlib.dates import date2num, WeekdayLocator, MONDAY, MonthLocator,\
    DateFormatter, DayLocator
from matplotlib import pyplot as plt
from matplotlib.pylab import figure, show
from scipy.stats.stats import pearsonr
from scipy.spatial.distance import euclidean
import csv

start_date = '2011-02-15 00:00:00'
end_date = '2011-02-20 23:00:00'

buy_prices, buy_volumes, times = get_data(start_date, end_date, type='buy')
sell_prices, sell_volumes, _ = get_data(start_date, end_date, type='sell')


# every monday
mondays   = WeekdayLocator(MONDAY)

# every month
months    = MonthLocator(range(1,13), bymonthday=1, interval=1)
days      = DayLocator(bymonthday=range(1,32))
monthsFmt = DateFormatter("%b '%y")
daysFmt   = DateFormatter("%d.%m")




volumes = list()
prices = list()
buy_volumes_min = list()
buy_volumes_max = list()

sell_volumes_min = list()
sell_volumes_max = list()

buy_volume_diff = list()

modified_times = list()
buy_lengths = list()
sell_lengths = list()

csv_rows_buy = list()
csv_rows_sell = list()

for i in range(0, len(buy_prices)):
    
    x_buy = [r for r in buy_volumes[i]]
    y_buy = [r for r in buy_prices[i]]

    x_sell = [r for r in sell_volumes[i]]
    y_sell = [r for r in sell_prices[i]]
    
    intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell, time=str(times[i][0]))
    
    '''buy_volumes_min.append(min(buy_volumes[i]))
    buy_volumes_max.append(max(buy_volumes[i]))
    sell_volumes_min.append(min(sell_volumes[i]))
    sell_volumes_max.append(max(sell_volumes[i]))
    '''
    
    #Line lengths
    length = 0
    for j in range(0, len(buy_volumes[i])-1):
        length += euclidean([buy_volumes[i][j], buy_prices[i][j]],[buy_volumes[i][j+1], buy_prices[i][j+1]])
    buy_lengths.append(length)
    
    '''length = 0
    for j in range(0, len(sell_volumes[i])-1):
        length += euclidean([sell_volumes[i][j], sell_prices[i][j]],[sell_volumes[i][j+1], sell_prices[i][j+1]])
    sell_lengths.append(length)'''
    
    #buy_volume_diff.append(max(buy_volumes[i]) - min(buy_volumes[i]))
    
    '''if intersect_y > 120:
        modified_times.append(times[i])
        x_sell = [x + 5000 for x in x_sell]
        intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell, time=str(times[i][0]))
    '''
    volumes.append(intersect_x)
    prices.append(intersect_y)

    '''csv_rows_buy.append([str(times[i][0]), min(buy_volumes[i]), max(buy_volumes[i]), max(buy_volumes[i])-min(buy_volumes[i]), length, intersect_x[0], intersect_y[0]])
    
    length = 0
    for j in range(0, len(buy_volumes[i])-1):
        length += euclidean([sell_volumes[i][j], sell_prices[i][j]],[sell_volumes[i][j+1], sell_prices[i][j+1]])
    sell_lengths.append(length)
    
    csv_rows_sell.append([str(times[i][0]), min(sell_volumes[i]), max(sell_volumes[i]), max(sell_volumes[i])-min(sell_volumes[i]), length, intersect_x[0], intersect_y[0]])
    '''
#write data to csv
'''with open("2011_buy_curve_data.csv", 'ab') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["time", "min_volume", "max_volume", "volume_difference", "curve_length", "system_price", "system_volume"])
        for item in csv_rows_buy:
            wr.writerow(item)
        csvfile.close()
        
with open("2011_sell_curve_data.csv", 'ab') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["time", "min_volume", "max_volume", "volume_difference", "curve_length", "system_price", "system_volume"])
        for item in csv_rows_sell:
            wr.writerow(item)
        csvfile.close()
'''
    

times_num = [date2num(t) for t in times]  
modified_times = [date2num(t) for t in modified_times]
modified_y = [50 for t in modified_times]  
fig = figure()
#f, axarr = plt.subplots(2, sharex=True)
#axarr[0].plot_date(times, buy_volumes_min, 'b-')
#axarr[0].plot_date(times, buy_volumes_max, 'r-')
#axarr[0].plot_date(times, prices, 'b-', label='System price')
#axarr[0].plot_date(modified_times, modified_y, 'ro')
#axarr[0].set_title('Sharing X axis')
#axarr[1].plot_date(times, volumes, 'g-', label='System volume')
ax = fig.add_subplot(111)
#ax2 = fig.add_subplot(211)
#ax.plot_date(times, buy_volume_diff, 'b-')
ax.plot(volumes, , 'r-')
ax.plot_date(times, prices, 'r-')
'''ax.plot_date(times_num[buy_lengths.index(max(buy_lengths))], max(buy_lengths), 'bo')
ax.plot_date(times_num[buy_lengths.index(min(buy_lengths))], min(buy_lengths), 'bo')
ax.annotate(str(times[buy_lengths.index(max(buy_lengths))][0]) +','+ str(max(buy_lengths)), xy=(times_num[buy_lengths.index(max(buy_lengths))], max(buy_lengths)), 
            xytext=(times_num[buy_lengths.index(max(buy_lengths))], max(buy_lengths)+200))
ax.annotate(str(times[buy_lengths.index(min(buy_lengths))][0]) +','+ str(min(buy_lengths)), xy=(times_num[buy_lengths.index(min(buy_lengths))], min(buy_lengths)), 
            xytext=(times_num[buy_lengths.index(min(buy_lengths))], min(buy_lengths)-200))
ax.set_title("2011 hourly sell curve lengths")
'''
#print str(times[buy_volumes_max.index(max(buy_volumes_max))][0]), max(buy_volumes_max)
#print str(times[buy_volumes_max.index(min(buy_volumes_max))][0]), min(buy_volumes_max)
#print pearsonr(buy_volumes_min, buy_volumes_max)
#ax2.plot_date(times, volumes, 'r-')
#ax.xaxis.set_major_locator(months)
#axarr[0].xaxis.set_major_locator(days)
#axarr[0].xaxis.set_major_formatter(daysFmt)

#axarr[0].xaxis.set_major_locator(months)
#axarr[0].xaxis.set_major_formatter(monthsFmt)

#axarr[0].grid(True)
#axarr[1].grid(True)
#axarr[0].legend(loc='best')
#axarr[1].legend(loc='best')


#ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(monthsFmt)
#ax.xaxis.set_major_formatter(daysFmt)
ax.xaxis.set_minor_locator(mondays)
ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
ax.grid(True)

#ax2.xaxis.set_major_formatter(monthsFmt)
#ax.xaxis.set_major_formatter(daysFmt)
#ax2.xaxis.set_minor_locator(mondays)
#ax2.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
#ax2.grid(True)

fig.autofmt_xdate()
show()
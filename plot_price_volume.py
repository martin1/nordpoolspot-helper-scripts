import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize.minpack import fsolve
from numpy.lib.function_base import interp
from data import *
from data import get_intersection_point
from matplotlib.dates import date2num


#following curves do not intersect:
#start_date = '2011-02-21 07:00:00'
#end_date = '2011-02-21 07:00:00'

start_date = '2011-02-21 10:00:00'
end_date = '2011-02-21 10:00:00'
hour = '01:00:00'

buy_prices, buy_volumes, times = get_data(start_date, end_date, type='buy', specified_hour = None)
sell_prices, sell_volumes, _ = get_data(start_date, end_date, type='sell', specified_hour = None)

modified_x = list()
modified_y = list()
#print len(times)
#print len(buy_prices)

#times = [date2num(t) for t in times]
#print str(times[1][0])
for i in range(0, len(buy_prices)):
    #print i
    x_buy = [r for r in buy_volumes[i]]
    y_buy = [r for r in buy_prices[i]]

    x_sell = [r for r in sell_volumes[i]]
    x_sell_5000 = [r+5000 for r in x_sell]
    
    y_sell = [r for r in sell_prices[i]]

    f_buy = lambda x: interp(x, x_buy, y_buy)
    f_sell = lambda x: interp(x, x_sell, y_sell)
   
    #intersect_x = fsolve(lambda x : f_sell(x) - f_buy(x), 10000)
    
    #plt.plot(x_buy, f_buy(x_buy), 'g.')
    #plt.plot(x_sell, f_sell(x_sell), 'b.')
    #print str(times[i][0])
    intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell, time=str(times[i][0]))
    modified_intersect_x, modified_intersect_y = get_intersection_point(x_buy, y_buy, x_sell_5000, y_sell, time=str(times[i][0]))
    
    '''if intersect_y > 150:
        x_sell = [x + 5000 for x in x_sell]
        modified_x
        intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell, time=str(times[i][0]))
    '''    
        
    plt.plot(intersect_x, intersect_y, 'go')
    plt.plot(x_buy, f_buy(x_buy), 'b-')#, linewidth=0.2, markersize=0.1)
    plt.plot(x_sell, f_sell(x_sell), 'r-')
    plt.plot(x_sell_5000, f_sell(x_sell), 'r--', label='f_sell + 5000')
    plt.plot(modified_intersect_x, modified_intersect_y, 'ro')
    plt.annotate(str(modified_intersect_x[0])+ ', ' + str(modified_intersect_y[0]), xy=(modified_intersect_x, modified_intersect_y),
                 xytext=(modified_intersect_x-3000, modified_intersect_y-100))
    print modified_intersect_x, modified_intersect_y
    #plt.title("2011-02-21 07:00")
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    #plt.plot(x_sell, f_sell(x_sell), 'r-', label='f_sell')#, linewidth=0.2, markersize=0.1)
    #plt.legend(loc='best')
    
plt.yticks(np.arange(-200, 2000, 100.0))
#plt.xticks(np.arange(10000, 55001, 5000))
plt.grid()
#plt.savefig("/home/martin/Dropbox/NordPoolSpot/curve_shapes/"+ )
plt.show()
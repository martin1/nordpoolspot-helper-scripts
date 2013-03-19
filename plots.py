from data import *
import matplotlib.pyplot as plt
import numpy as np



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
   
            intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell, time=str(times[i][0]))
            plt.plot(intersect_x, intersect_y, 'go')
            
        plt.plot(x_buy, f_buy(x_buy), 'b-')#, linewidth=0.2, markersize=0.1)
        plt.plot(x_sell, f_sell(x_sell), 'r-')
        plt.annotate(str(intersect_x[0])+ ', ' + str(intersect_y[0]), xy=(intersect_x, intersect_y),
                     xytext=(intersect_x-3000, intersect_y-100))
    
    plt.yticks(np.arange(-200, 2000, 100.0))
    plt.grid()
    plt.show()

def plot_time_price():
    pass

def plot_time_volume():
    pass

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

########################################
start_date = '2011-02-21 10:00:00'
end_date = '2011-02-21 11:00:00'
hour = '01:00:00'

buy_prices, buy_volumes, times = get_data(start_date, end_date, type='buy', specified_hour = None)
sell_prices, sell_volumes, _ = get_data(start_date, end_date, type='sell', specified_hour = None)

plot_price_volume(buy_prices, buy_volumes, sell_prices, sell_volumes, show_intersections=True)
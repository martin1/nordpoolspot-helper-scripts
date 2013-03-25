from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
from data import *
from scipy.interpolate import interp1d


def get_avg_func(x, y, points=1000):
    y_avg = linspace(2000, -200, points)
    #y_avg = [2000]
    print y_avg[0]
    x_avg = list()
    
    for i in range(0, len(y_avg)):#for every point in the new average curve...
        element = 0
        print i
        for j in range(0, len(x)):#for every curve: get the inverse function
            f = get_inverse_function(x[j], y[j])
            element += f(y_avg[i])
            print element
        x_avg.append(element/len(x))
        
    return lambda x: interp(x, x_avg, y_avg), x_avg
            

def get_func(x_list, y_list):
    return lambda x: interp(x, x_list, y_list)

def get_inverse_function(x_list, y_list):
    x_inv = sorted(x_list, reverse=True)
    y_inv = sorted(y_list, reverse=False)
    return lambda x: interp(x, y_inv, x_inv)
    #return interp1d(y_inv, x_inv, bounds_error=False)

start_date = '2011-01-01 05:00:00'
end_date = '2011-02-01 23:00:00'
    
buy_prices, buy_volumes, _ = get_data(start_date, end_date, type='buy', specified_hour=None)

x = list()
y = list()

for i in range(0, len(buy_prices)):
    #print i
    x_buy = [r for r in buy_volumes[i]]
    y_buy = [r for r in buy_prices[i]]
    
    x.append(x_buy)
    y.append(y_buy)
    
print x[0]
print x[15]
plt.plot(x[0], y[0], 'b-')
plt.plot(x[15], y[15], 'r-')
f_avg, x_avg = get_avg_func([x[0], x[15]], [y[0], y[15]], points = 1000)
plt.plot(x_avg, f_avg(x_avg), 'g-')        



plt.show()


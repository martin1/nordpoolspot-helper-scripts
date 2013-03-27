from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
from data import *
from scipy.interpolate import interp1d


def get_avg_func(x, y, points=1000):
    
    y_max = 2000.0
    y_min = -200.0
    
    y_avg = linspace(y_max, y_min, points)
    x_avg = list()
    f = list()
    
    #get inverse functions for all curves
    for i in range(0, len(x)):
            f.append(get_inverse_function(x[i], y[i]))
    
    
    for i in range(0, len(y_avg)):#for every point in the new average curve...
        element = 0
        for j in range(0, len(x)):#for every curve: get the inverse function
            element += f[j](y_avg[i])
        x_avg.append(element/len(x))
        
    return lambda x: interp(x, x_avg, y_avg), x_avg
            

def get_func(x_list, y_list):
    return lambda x: interp(x, x_list, y_list)

def get_inverse_function(x_list, y_list):
    x_inv = sorted(x_list, reverse=True)
    y_inv = sorted(y_list, reverse=False)
    return lambda x: interp(x, y_inv, x_inv)
    #return interp1d(y_inv, x_inv, bounds_error=False)
    
def get_distance(x1, y1, x2, y2, points=10000):
    
    y_max = 2000.0
    y_min = -200.0
    
    f1_inv = get_inverse_function(x1, y1)
    f2_inv = get_inverse_function(x2, y2)
    
    y = linspace(y_max, y_min, points)
    
    dist = list()
    dist_y = list()
    min_points = list()
    max_points = list()
    
    for y_n in y:
        d = abs(f1_inv(y_n) - f2_inv(y_n))
        dist.append(d)
    
    max_y = y[dist.index(max(dist))]
    min_y = y[dist.index(min(dist))]
    dist = [max(dist), min(dist), sum(dist)/float(len(dist))]
    min_points = [[f1_inv(min_y), min_y],[f2_inv(min_y), min_y]]
    max_points = [[f1_inv(max_y), max_y],[f2_inv(max_y), max_y]]
    
    return dist, min_points, max_points
    


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
    
'''print x[0]
print x[15]
print x[20]
plt.plot(sorted(x[0]), sorted(y[0], reverse=True), 'b-')
plt.plot(sorted(x[15]), sorted(y[15], reverse=True), 'r-')
plt.plot(sorted(x[20]), sorted(y[20], reverse=True), 'b--')
f_avg, x_avg = get_avg_func([x[0], x[15], x[20]], [y[0], y[15], y[20]], points = 10000)
plt.plot(x_avg, f_avg(x_avg), 'g-')        
print x_avg[0]'''

dist, min_points, max_points = get_distance(x[0], y[0], x[15], y[15])
plt.plot(x[0], y[0], 'b-')
plt.plot(x[15], y[15], 'r-')
plt.plot([min_points[0][0], min_points[1][0]],[min_points[0][1], min_points[1][1]], 'go')
plt.plot([max_points[0][0], max_points[1][0]],[max_points[0][1], max_points[1][1]], 'ro')
print dist[2]

plt.show()


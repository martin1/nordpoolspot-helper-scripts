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
    avg_dist = list()
    
    #get inverse functions for all curves
    for i in range(0, len(x)):
            f.append(get_inverse_function(x[i], y[i]))
    
    
    for i in range(0, len(y_avg)):#for every point in the new average curve...
        element = 0
        for j in range(0, len(x)):#for every curve: get the inverse function
            element += f[j](y_avg[i])
        x_avg.append(element/len(x))
    
    '''for i in range(0, len(x)):
        avg_dist.append(get_distance(x[i], y[i], x_avg, y_avg, show_direction=False)[2])'''
    return lambda x: interp(x, x_avg, y_avg), x_avg#, avg_dist
            

def get_func(x_list, y_list):
    return lambda x: interp(x, x_list, y_list)

def get_inverse_function(x_list, y_list):
    x_inv = sorted(x_list, reverse=True)
    y_inv = sorted(y_list, reverse=False)
    return lambda x: interp(x, y_inv, x_inv)
    #return interp1d(y_inv, x_inv, bounds_error=False)
    
def get_distance(x1, y1, x2, y2, points=10000, show_direction = False):
    
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
        if show_direction == False:
            d = abs(f1_inv(y_n) - f2_inv(y_n))
        elif show_direction == True:
            d = f1_inv(y_n) - f2_inv(y_n)
        dist.append(d)
    
    max_y = y[dist.index(max(dist))]
    min_y = y[dist.index(min(dist))]
    dist = [max(dist), min(dist), sum(dist)/float(len(dist))]
    min_points = [[f1_inv(min_y), min_y],[f2_inv(min_y), min_y]]
    max_points = [[f1_inv(max_y), max_y],[f2_inv(max_y), max_y]]
    
    return dist, min_points, max_points

def predict_curve(time_str, curve_type='buy', base_curves=7):
    #get last 7 days curves for specified hour
    fmt = "%Y-%m-%d %H:%M:%S"
    max_time = datetime.datetime.strptime(time_str, fmt) - datetime.timedelta(days=1)
    max_time_str = datetime.datetime.strftime(max_time, fmt)
    hour = time_str.partition(" ")[2]
    min_time = max_time - datetime.timedelta(days=base_curves-1)
    min_time_str = datetime.datetime.strftime(min_time, fmt)
    #get the data
    print max_time_str
    print min_time_str
    prices, volumes, times = get_data(min_time_str, time_str, type=curve_type, specified_hour=hour)
    #get average curve
    f_avg, x_avg = get_avg_func(volumes, prices, points=10000)
    
    dist = list()
    
    for i in range(0, len(volumes)):
        dist.append(get_distance(volumes[i], prices[i], x_avg, f_avg(x_avg), points=1000, show_direction = False)[0][2])
        #print dist[i]
    return x_avg, f_avg, dist
    


'''start_date = '2011-01-01 05:00:00'
end_date = '2011-01-01 06:00:00'
    
buy_prices, buy_volumes, _ = get_data(start_date, end_date, type='buy', specified_hour=None)

x = list()
y = list()

for i in range(0, len(buy_prices)):
    #print i
    x_buy = [r for r in buy_volumes[i]]
    y_buy = [r for r in buy_prices[i]]
    
    x.append(x_buy)
    y.append(y_buy)

#f_avg, x_avg = get_avg_func([x[0], x[15]], [y[0], y[15]])
f_avg, x_avg = get_avg_func(buy_volumes, buy_prices)
print x_avg    
dist, min_points, max_points = get_distance(x[0], y[0], x[15], y[15])
plt.plot(x[0], y[0], 'b-')
plt.plot(x[15], y[15], 'r-')
plt.plot(x_avg, f_avg(x_avg), 'g-')
plt.plot([min_points[0][0], min_points[1][0]],[min_points[0][1], min_points[1][1]], 'go')
plt.plot([max_points[0][0], max_points[1][0]],[max_points[0][1], max_points[1][1]], 'ro')
print dist[2]

plt.show()'''

prediction_time = '2011-03-11 12:00:00'    
x_avg, f_avg, dist = predict_curve(prediction_time, curve_type='buy', base_curves=7)

start_date = prediction_time
end_date = prediction_time
    
buy_prices, buy_volumes, _ = get_data(start_date, end_date, type='buy', specified_hour=None)

#last_prices, last_volumes, _ = get_data('2011-01-30 05:00:00', '2011-01-30 05:00:00', type='buy', specified_hour=None)
#plt.plot(last_volumes[0], last_prices[0], 'go')
#x = [x+1359.95 for x in buy_volumes[0]]
plt.plot(x_avg, f_avg(x_avg), 'b-', label='Predicted')
plt.plot(buy_volumes[0], buy_prices[0], 'r-', label='Actual')
#plt.plot(x, buy_prices[0], 'r-')
plt.legend(loc='best')
plt.title("Buy curve 2011-03-11 12:00:00")
plt.plot()
for i in range(0, len(dist)): print 'avg - ' + str(i) +' '+ str(dist[i])
print '----------------'
print get_distance(buy_volumes[0], buy_prices[0], x_avg, f_avg(x_avg), points=1000, show_direction=False)[0][2]
plt.show()


from numpy.core.function_base import linspace
import matplotlib.pyplot as plt
from data import *
from scipy.interpolate import interp1d


'''def plot_max_distance(f1, f2):
    
    y = linspace(-200, 2000, num=100)
    f1_inv = get_inverse_function
    
    x1 = [f1(value) for value in y]
    x2 = [f2(value) for value in y]
    
    #calculate distances between horisontally aligned points on f1 and f2
    max_dist = 0
    index = 0
    for i in range(0, len(x1)):
        if abs(x1[i]-x2[i]) > max_dist:
            max_dist = abs(x1[i]-x2[i])
            index = i 
    print max_dist        
    plt.plot(x1, f1(x1), 'b-')
    plt.plot(x2, y, 'r-')
    #plt.plot([x1[index],x2[index]], [y[index], y[index]], 'g-')
    plt.show()
'''

def get_func(x_list, y_list):
    return lambda x: interp(x, x_list, y_list)

'''Order of Y!!!!!!!!!!'''
def get_inverse_function(x_list, y_list):
    #return lambda x: interp(x, y_list, x_list)
    return interp1d(x_list, y_list, bounds_error=False)

start_date = '2011-01-01 05:00:00'
end_date = '2011-01-01 05:00:00'
    
buy_prices, buy_volumes, _ = get_data(start_date, end_date, type='buy', specified_hour=None)

f = list()
x = list()
y = list()
x_min = list()
x_max = list()
for i in range(0, len(buy_prices)):
        x_buy = [r for r in buy_volumes[i]]
        y_buy = [r for r in buy_prices[i]]
        x.append(x_buy)
        y.append(y_buy)
        x_min.append(min(x_buy))
        x_max.append(max(x_buy))
        


x1 = linspace(x_min[0], x_max[0], 10000)
#x15 = linspace(x_min[14], x_max[14], 10000)
#x_avg = linspace((x_min[0] + x_min[14])/2, (x_max[0] + x_max[14])/2, 10000)

f1 = get_func(x[0], y[0])
#f15 = get_func(x[14], y[14])
x_inv = sorted(x[0], reverse=True)
y_inv = sorted(y[0], reverse=False)
#f_inv = get_inverse_function(x_inv, y_inv)
f_inv = interp1d(y_inv, x_inv)

print x[0][0], y[0][0]
print f1(30762.593538)
print f_inv(2000)
#print x_inv
#print y_inv
#print '--'
#print x[0]
#print y[0]
#plt.plot(x1, f_inv(x1))
#plt.plot(x1, f1(x1), 'b-')
#plt.plot(x[0], f_inv(x[0]))
#plt.plot(x15, f15(x15), 'r-')
#plt.plot(x_avg, (f1(x_avg) + f15(x_avg))/2, 'g-')
#plt.plot(f_inv(y[0]), x[0])

diff1 = x_max[0] - x_min[0]
#diff15 = x_max[14] - x_min[14]
#print diff1
#print diff15

plt.show()


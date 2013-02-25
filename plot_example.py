'''
Created on Feb 21, 2013

@author: martin
'''


import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import legend, axes
from scipy.interpolate.interpolate import interp1d
from numpy.core.numeric import arange
import pymysql
from scipy.interpolate.fitpack import splrep, splev
from scipy.interpolate.fitpack2 import InterpolatedUnivariateSpline,\
    UnivariateSpline
from numpy.core.function_base import linspace
from scipy.optimize.minpack import fsolve

con = pymysql.connect(host='127.0.0.1', unix_socket = '/run/mysqld/mysqld.sock', user = 'root', passwd = 'martyn', db = 'martin_kurgi')
cur = con.cursor()
cur.execute("select time from chart_data where time = '2011-01-01 00:00:00' or time = '2011-01-01 00:00:00'")
times = cur.fetchall()
buy_prices = []
buy_volumes = []
sell_prices = []
sell_volumes = []
for time in times:
    time_str = datetime.datetime.strftime(time[0], '%Y-%m-%d %H:%M:%S')
    print(time_str)
    query1 = "select price, volume from buy_price_volume where time = " + "'"+ time_str + "' order by volume asc"
    print(query1)
    cur.execute(query1)
    result = cur.fetchall()
    buy_prices.append([r[0] for r in result])
    buy_volumes.append([r[1] for r in result])
    query2 = "select price, volume from sell_price_volume where time = " + "'"+ time_str + "' order by volume asc"
    cur.execute(query2)
    result = cur.fetchall()
    sell_prices.append([r[0] for r in result])
    sell_volumes.append([r[1] for r in result])
con.close()

#for item in buy_prices:

x_buy = [r for r in buy_volumes[0]]
y_buy = [r for r in buy_prices[0]]

x_sell = [r for r in sell_volumes[0]]
y_sell = [r for r in sell_prices[0]]

#x_buy = [1,3,3.04,3.67,5,8,9]
#y_buy = [3,6,9,2, 5, 3, 2]

#x1 = sorted([r for r in sell_volumes[0]])
#y1 = sorted([r for r in sell_prices[0]], reverse=False)

print(x_buy)
print(y_buy)

f_buy = interp1d(x_buy, y_buy, kind = 'linear')
f_sell = interp1d(x_sell, y_sell, kind = 'linear')
#fsolve()    

new_x_buy = linspace(min(x_buy), max(x_buy), 1000)
new_x_sell = linspace(min(x_sell), max(x_sell), 1000)

#for x_buy in new_x:
#    print f(x_buy)


#f = InterpolatedUnivariateSpline(x_buy,y_buy)


#plt.plot(new_x, f(new_x),'b-')
#print 
#for time in times:
#    time = date2num(time)
plt.plot(new_x_buy, f_buy(new_x_buy), 'g')
plt.plot(new_x_sell, f_sell(new_x_sell), 'b')
plt.plot(fsolve(lambda x : f_buy(x) - f_sell(x),35000), f_buy(fsolve(lambda x : f_buy(x) - f_sell(x),35000)), 'x')
#plt.plot(x_buy,y_buy, 'bo')
#plt.plot(x,y, 'rx')
plt.show()
#print(f_buy(fsolve(lambda x : f_buy(x) - f_sell(x),35000)))
'''fig = plt.figure()
#axes.set_default_color_cycle(['b', 'g', 'r', 'c'])
for i in range(0, len(buy_volumes)):
    if i == 0: plt.plot(buy_volumes[i], buy_prices[i], label = 'Purchase 2011-01-01 00:00:00', linewidth = 1.0)
    plt.plot(buy_volumes[i], buy_prices[i], 'bo')
    
for i in range(0, len(sell_volumes)):   
    if i == 0: legend_sell = plt.plot(sell_volumes[i], sell_prices[i], label = 'Purchase 2011-01-01 00:00:00', linewidth=1.0) 
    plt.plot(sell_volumes[i], sell_prices[i], 'ro')

plt.yticks(np.arange(-200, 2000, 100.0))
plt.xticks(np.arange(20000, 70001, 2000))
plt.grid()
plt.title("2011-01-01 00:00:00 - 2011-01-31 23:00:00")
plt.legend(loc='best')
plt.show()
'''
''''x_buy = np.arange(0,2*np.pi+np.pi/4,2*np.pi/8)
y_buy = np.sin(x_buy)
s = InterpolatedUnivariateSpline(x_buy,y_buy)
xnew = np.arange(0,2*np.pi,np.pi/50)
ynew = s(xnew)
plt.figure()
plt.plot(x_buy,y_buy,'x_buy',xnew,ynew,xnew,np.sin(xnew),x_buy,y_buy,'b')
plt.legend(['Linear','InterpolatedUnivariateSpline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('InterpolatedUnivariateSpline')
plt.show()
'''
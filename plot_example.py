'''
Created on Feb 21, 2013

@author: martin
'''


import datetime
import matplotlib.pyplot as plt
import numpy as np
import pymysql
from scipy.optimize.minpack import fsolve
from numpy.lib.function_base import interp


#####################
#Database connection
#####################

con = pymysql.connect(host='127.0.0.1', unix_socket = '/run/mysqld/mysqld.sock', user = 'root', passwd = 'martyn', db = 'martin_kurgi')
cur = con.cursor()
cur.execute("select time from chart_data where time between '2011-01-01 00:00:00' and '2011-01-01 23:00:00'")
times = cur.fetchall()
buy_prices = []
buy_volumes = []
sell_prices = []
sell_volumes = []
for time in times:
    time_str = datetime.datetime.strftime(time[0], '%Y-%m-%d %H:%M:%S')
    print(time_str)
    query1 = "select price, volume from buy_price_volume where time = " + "'"+ time_str + "' order by volume asc"
    #print(query1)
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

for i in range(0, len(buy_prices)):
    
    x_buy = np.array([r for r in buy_volumes[i]])
    y_buy = [r for r in buy_prices[i]]

    x_sell = np.array([r for r in sell_volumes[i]])
    y_sell = [r for r in sell_prices[i]]

    f_buy = lambda x: interp(x, x_buy, y_buy)
    f_sell = lambda x: interp(x, x_sell, y_sell)
   
    intersect_x = fsolve(lambda x : f_sell(x) - f_buy(x), 10000)
    
    plt.plot(x_buy, f_buy(x_buy), 'g')
    plt.plot(x_sell, f_sell(x_sell), 'b')
    
    plt.plot(intersect_x, f_buy(intersect_x), 'rx')
    
plt.yticks(np.arange(-200, 2000, 100.0))
plt.xticks(np.arange(20000, 55001, 5000))
plt.grid()
plt.show()
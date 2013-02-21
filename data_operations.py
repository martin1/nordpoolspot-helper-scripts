#coding=utf-8

import datetime
from matplotlib.dates import MonthLocator, DateFormatter, DayLocator,\
    DateLocator, WeekdayLocator, MONDAY
from matplotlib import pylab
from matplotlib.pyplot import legend

''''ssh tunnel: ssh -N -p 1521 [username]@[host] -L 9990:127.0.0.1:3306'''

import MySQLdb
import matplotlib.pyplot as plt
import matplotlib.dates as d
from pylab import figure, show
import numpy

con = MySQLdb.connect(host='localhost', user = 'root', passwd = '[passwd]', db = 'martin_kurgi', port = 3306)
cur = con.cursor()
cur.execute("select distinct date from chart_data where date between '2011-01-01' and '2013-01-01'")
times = cur.fetchall()
buy_prices = []
sell_prices = []
buy_prices_times = []
sell_prices_times = []
times_chart = []  
for time in times:
    time_str = datetime.datetime.strftime(time[0], '%Y-%m-%d')
    print time_str
    query1 = "select volume from buy_price_volume where date = " + "'"+ time_str + "'"
    #print query
    cur.execute(query1)
    #times_chart.append(time_str.split(' ')[0])
    buy_prices_times = cur.fetchall()
    buy_prices.append(numpy.mean(buy_prices_times))
    
    query2 = "select volume from sell_price_volume where date = " + "'"+ time_str + "'"
    cur.execute(query2) 
    sell_prices_times = cur.fetchall()
    sell_prices.append(numpy.mean(sell_prices_times))
    
for time in times:
    times_chart.append(d.date2num(time))

con.close()

# every monday
mondays   = WeekdayLocator(MONDAY)

# every 3rd month
months    = MonthLocator(range(1,13), bymonthday=1, interval=1)
monthsFmt = DateFormatter("%b '%Y")

fig = figure()
ax = fig.add_subplot(111)
ax.plot_date(times_chart, buy_prices, 'b-', label='Volume (buy)')
ax.plot_date(times_chart, sell_prices, 'r-', label='Volume (sell)')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.xaxis.set_minor_locator(mondays)
ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
ax.grid(True)
legend()

fig.autofmt_xdate()

show()                                                                                                   

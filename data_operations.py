#coding=utf-8

import datetime
from matplotlib.dates import MonthLocator, DateFormatter, DayLocator,\
    DateLocator, WeekdayLocator, MONDAY
from matplotlib.pyplot import legend

''''ssh tunnel: ssh -N -p 1521 [username]@[host] -L 9990:127.0.0.1:3306'''

import MySQLdb
import matplotlib.dates as d
from pylab import figure, show
import numpy

con = MySQLdb.connect(host='localhost', user = 'root', passwd = 'martyn', db = 'martin_kurgi', port = 3306)
cur = con.cursor()
cur.execute("select distinct time from chart_data where time between '2011-08-01 00:00:00' and '2011-08-31 23:00:00'")
times = cur.fetchall()
buy_prices = []
sell_prices = []
buy_prices_times = []
sell_prices_times = []
times_chart = []  
for time in times:
    time_str = datetime.datetime.strftime(time[0], '%Y-%m-%d %H:%M:%S')
    print time_str
    query1 = "select price from buy_price_volume where time = " + "'"+ time_str + "'"
    #print query
    cur.execute(query1)
    #times_chart.append(time_str.split(' ')[0])
    buy_prices_times = cur.fetchall()
    buy_prices.append(numpy.mean(buy_prices_times))
    
    query2 = "select price from sell_price_volume where time = " + "'"+ time_str + "'"
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
days      = DayLocator(bymonthday=range(1,32))
dateFmt   = DateFormatter("%d %b")
monthsFmt = DateFormatter("%b '%Y")

fig = figure()
ax = fig.add_subplot(111)
ax.plot_date(times_chart, buy_prices, 'b-', label='Volume (buy)')
ax.plot_date(times_chart, sell_prices, 'r-', label='Volume (sell)')
#ax.xaxis.set_major_locator(months)
#ax.xaxis.set_major_formatter(monthsFmt)
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(dateFmt)
#ax.xaxis.set_minor_locator(mondays)
ax.yaxis.set_label_text("EUR/MWh")
ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
ax.grid(True)
legend(loc=4)

fig.autofmt_xdate()

show()                                                                                                   

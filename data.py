import datetime
import MySQLdb
from numpy.lib.function_base import interp
from scipy.optimize.minpack import fsolve

def get_data(time_start, time_end, type='buy', specified_hour=None) :
    con = MySQLdb.connect(host='localhost', user = 'root', passwd = '', db = 'martin', port = 3306)
    cur = con.cursor()
    if specified_hour is None:
        cur.execute("select time from chart_data where time between '" + time_start + "' and '" + time_end + "'")
    elif specified_hour is not None:
        cur.execute("select time from chart_data where time between '" + time_start + "' and '" + time_end + "' and time(time) = '" + specified_hour + "'")
        print "select time from chart_data where time between '" + time_start + "' and '" + time_end + "' and time(time) = '" + specified_hour + "'"
    times = cur.fetchall()

    if type == 'buy': #return both buy and sell prices
        db_table = 'buy_price_volume'
    elif type == 'sell':
        db_table = 'sell_price_volume'
    prices = []
    volumes = []    
    for time in times:
        time_str = datetime.datetime.strftime(time[0], '%Y-%m-%d %H:%M:%S')
        print("data-[" + type + "]-:" + time_str)
        query = "select price, volume from " + db_table + " where time = " + "'"+ time_str + "' order by volume asc"
        #print(query)
        cur.execute(query)
        result = cur.fetchall()
        prices.append([r[0] for r in result])
        volumes.append([r[1] for r in result])
    con.close()
    return prices, volumes, times

def get_intersection_point(buy_x_list, buy_y_list, sell_x_list, sell_y_list, time=None):#, fix_data=True):
    
    '''if fix_data == True: # apply fix for data
        corrected_data = {'2011-02-21 07:00:00':[48500, 73.32],
                          '2011-02-21 09:00:00':[49000, 73.3],
                          '2011-02-21 08:00:00':[49400, 75.26]}
        for key in corrected_data.keys():
            if key == time:
                return corrected_data[key]
    #end if'''
    #calculate intersection point
    f_buy = lambda x: interp(x, buy_x_list, buy_y_list)
    f_sell = lambda x: interp(x, sell_x_list, sell_y_list)
        
    intersect_x = fsolve(lambda x : f_sell(x) - f_buy(x), 10000)
    return [intersect_x, f_buy(intersect_x)]

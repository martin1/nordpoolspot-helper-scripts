import datetime
import MySQLdb
from numpy.lib.function_base import interp
from scipy.optimize.minpack import fsolve

#####################
#Database connection
#####################



def get_data(time_start, time_end, prices='buy') :
    con = MySQLdb.connect(host='localhost', user = 'root', passwd = 'martyn', db = 'martin_kurgi', port = 3306)
    cur = con.cursor()
    cur.execute("select time from chart_data where time between '" + time_start + "' and '" + time_end + "'")
    times = cur.fetchall()

    if prices == 'buy': #return both buy and sell prices
        db_table = 'buy_price_volume'
    elif prices == 'sell':
        db_table = 'sell_price_volume'
    prices = []
    volumes = []    
    for time in times:
        time_str = datetime.datetime.strftime(time[0], '%Y-%m-%d %H:%M:%S')
        #print(time_str)
        query = "select price, volume from " + db_table + " where time = " + "'"+ time_str + "' order by volume asc"
        print(query)
        cur.execute(query)
        result = cur.fetchall()
        prices.append([r[0] for r in result])
        volumes.append([r[1] for r in result])
    con.close()
    return prices, volumes

def get_intersection_point(buy_x_list, buy_y_list, sell_x_list, sell_y_list):
    f_buy = lambda x: interp(x, buy_x_list, buy_y_list)
    f_sell = lambda x: interp(x, sell_x_list, sell_y_list)
    
    intersect_x = fsolve(lambda x : f_sell(x) - f_buy(x), 10000)
    
    return [intersect_x, f_buy(intersect_x)]
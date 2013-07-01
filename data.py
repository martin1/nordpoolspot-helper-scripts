import datetime
import MySQLdb
import psycopg2
from numpy.lib.function_base import interp
from scipy.optimize.minpack import fsolve

def get_curve(start_time, end_time, type='buy', specified_hour=None):
    con = psycopg2.connect(database="martin", user="postgres", password="postgres")
    cur = con.cursor()
    
    if type == 'buy':
        query = "SELECT time, buy_volumes, buy_prices, accepted_blocks_buy FROM curve WHERE time BETWEEN '" + start_time + "' and '" + end_time + "'"
    elif type == 'sell':
        query = "SELECT time, sell_volumes, sell_prices, accepted_blocks_sell + volume_net_flows FROM curve WHERE time BETWEEN '" + start_time + "' and '" + end_time + "'"
        
    #elif type == None:
     #   query = "SELECT time, buy_volumes, buy_prices, sell_volumes, sell_prices, accepted_blocks_buy, accepted_blocks_sell + volume_net_flows FROM curve WHERE time BETWEEN '" + start_time + "' and '" + end_time + "'"
    
    if specified_hour is not None:
        query += "and extract(hour, time) = " + specified_hour + "'"
        
    #order the results
    query += "ORDER BY time asc"
    
    cur.execute(query)
    result = cur.fetchall()
    times = [r[0] for r in result]
    volumes = [sorted(r[1]) for r in result]
    prices = [r[2] for r in result]
    adjustments = [r[3] for r in result]
    #print adjustments
    
    #make horizontal adjustments to curve data
    
    for n in range(0, len(volumes)):
        for i in range(0, len(volumes[n])):
            volumes[n][i] += float(adjustments[n])
    print "Data done"
    return prices, volumes, times

def get_intersection_point(buy_x_list, buy_y_list, sell_x_list, sell_y_list, time=None):#, fix_data=True):
    #calculate intersection point
    f_buy = lambda x: interp(x, buy_x_list, buy_y_list)
    f_sell = lambda x: interp(x, sell_x_list, sell_y_list)
        
    intersect_x = fsolve(lambda x : f_sell(x) - f_buy(x), 10000)
    return intersect_x, f_buy(intersect_x)

def get_system_price_volume(start_time, end_time):
    buy_prices, buy_volumes, times = get_curve(start_time, end_time, type='buy', specified_hour = None)
    sell_prices, sell_volumes, _ = get_curve(start_time, end_time, type='sell', specified_hour = None)
    
    prices = list()
    volumes = list()
    
    for i in range(0, len(buy_prices)):
        x_buy = [r for r in buy_volumes[i]]
        y_buy = [r for r in buy_prices[i]]
        
        x_sell = [r for r in sell_volumes[i]]
        y_sell = [r for r in sell_prices[i]]
        
        f_buy = lambda x: interp(x, x_buy, y_buy)
        f_sell = lambda x: interp(x, x_sell, y_sell)
        
        intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell)
        
        volumes.append(intersect_x[0])
        prices.append(round(intersect_y[0],2))
    
    return volumes, prices, times
    
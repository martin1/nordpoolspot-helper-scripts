from data import *
import datetime

def get_sysprice_list(start_time, end_time, frequency='hourly'):
#frequency one of [hourly, daily, monthly]

    _ , sys_prices, times = get_system_price_volume(start_time, end_time)
    
    def get_daily_sys_prices_times():
        pass
    
    if frequency == 'daily':
        daily_sys_prices = list()
        daily_sys_price = 0
        #convert times to dates
        times = [time.date() for time in times]
        for i in range(0, len(times)-1):
            if times[i] == times[i+1]:
                daily_sys_price += sys_prices[i]
                #last element in list
                '''if i+1 == len(times):
                    daily_sys_price += sys_prices[i+1]'''
            elif times[i] != times[i+1]:
                daily_sys_price += sys_prices[i]
                #Add hour 23-00 price
                #daily_sys_price += sys_prices[i]
                daily_sys_prices.append(round(daily_sys_price/times.count(times[i]),2))
                daily_sys_price = 0 
            if i+1 == len(times)-1:#last price in list
                print "last"
                daily_sys_price += sys_prices[i+1]
                daily_sys_prices.append(round(daily_sys_price/times.count(times[i+1]),2))   
        #remove duplicate date entries 
        times = sorted(list(set(times)))
        print daily_sys_prices
        print times

    elif frequency == 'monthly':
        pass
        
    
    #return sysprice_list

get_sysprice_list('2011-01-01 00:00:00', '2011-01-04 23:00:00', frequency='daily')
#print datetime.date(datetime.datetime(2013,6,26,12,0).year, datetime.datetime(2013,6,26,12,0).month, 1)
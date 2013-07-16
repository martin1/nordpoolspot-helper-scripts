from data import *
import datetime
import calendar
import pandas as pd

def get_daily_sys_prices_times(hourly_sys_prices, hourly_times):
    d = {}
    daily_sys_prices = list()
    daily_sys_price = 0
    #convert times to dates
    times = [time.date() for time in hourly_times]
    #print times
    
    for i in range(0, len(times)-1):
        if times[i] == times[i+1]:
            daily_sys_price += hourly_sys_prices[i]
        elif times[i] != times[i+1]:
            daily_sys_price += hourly_sys_prices[i]
            daily_sys_prices.append(round(daily_sys_price/times.count(times[i]),2))
            d[times[i]] = round(daily_sys_price/times.count(times[i]),2)
            daily_sys_price = 0 
        if i+1 == len(times)-1:#last price in list
            daily_sys_price += hourly_sys_prices[i+1]
            daily_sys_prices.append(round(daily_sys_price/times.count(times[i+1]),2))   
            d[times[i+1]] = round(daily_sys_price/times.count(times[i+1]),2)
    
    return [d[key] for key in sorted(d.keys())], sorted(d.keys())

'''def get_sysprice_list2(start_time, end_time, frequency='hourly'):
#frequency one of [hourly, daily, monthly]

    _ , hourly_sys_prices, hourly_times = get_system_price_volume(start_time, end_time)
    sys_prices, times = hourly_sys_prices, hourly_times
    
    if frequency == 'daily':
        sys_prices, times = get_daily_sys_prices_times(hourly_sys_prices, hourly_times)
    
    elif frequency == 'weekly':
        daily_sys_prices, daily_times = get_daily_sys_prices_times(hourly_sys_prices, hourly_times)
        
        weekly_sys_price = 0
        d={}
        
        for time in [time for time in daily_times if time.weekday() == 0]: #for every monday
            #get week number 
            if daily_times.index(time) + 6 <= len(daily_times):#Check if we have full week present in data
                for i in range(daily_times.index(time), daily_times.index(time) + 7):
                    weekly_sys_price += daily_sys_prices[i]
                    print daily_sys_prices[i]
                d[time] = round(weekly_sys_price/7,2)
                weekly_sys_price = 0
        sys_prices = [d[key] for key in sorted(d.keys())]
        times = [(key.year, key.isocalendar()[1]) for key in sorted(d.keys())]       

    elif frequency == 'monthly':
        daily_sys_prices, daily_times = get_daily_sys_prices_times(hourly_sys_prices, hourly_times)
        
        for i in range(0, len(daily_times)):
            print daily_times[i]
            print daily_sys_prices[i]
        
        monthly_sys_price = 0
        d = {}
        
        for time in [time for time in daily_times if time.day==1]:#find first of month
            current_month = time.month
            month_length = calendar.monthrange(time.year, current_month)[1]
            #Check if whole month is present in data - it is assumed that the data is continuous (no gaps in dates)
            if daily_times.index(time) + month_length <= len(daily_times):
                for i in range(daily_times.index(time), daily_times.index(time) + month_length):
                    monthly_sys_price += daily_sys_prices[i]
                d[time] = round(monthly_sys_price/month_length,2)
                monthly_sys_price = 0
        sys_prices = [d[key] for key in sorted(d.keys())]
        times = [(key.year, key.month) for key in sorted(d.keys())]        
        
    for i in range(0, len(times)):
        print times[i]
        print sys_prices[i]
    return times, sys_prices'''

def get_sysprice_list(start_time, end_time, frequency='hourly'):
    #frequency one of [hourly, daily, monthly]

    _ , sys_prices, times = get_system_price_volume(start_time, end_time)
    
    ts = pd.Series(sys_prices, index=times)
    resampling_frequency = None
    label_offset = None
    
    if frequency == 'daily':
        resampling_frequency = 'D'
    
    elif frequency == 'weekly':
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

        if start_time.date().weekday() != 0:
            raise ValueError(str(start_time.date())+ " is a " + start_time.date().strftime('%A') + ". start_date must be a Monday.")
        if end_time.date().weekday() != 6:
            raise ValueError(str(end_time.date())+ " is a " + end_time.date().strftime('%A') + ". end_date must be a Sunday.")
        resampling_frequency = 'W'     

    elif frequency == 'monthly':
        resampling_frequency = 'M'
    
    if resampling_frequency is not None:
        #Resampling must be done
        return ts.resample(resampling_frequency, how='mean', kind='period')
    else:
        #Resampling is not necessary
        return ts

#get_sysprice_list('2013-01-01 00:00:00', '2013-01-31 23:00:00', frequency='monthly')
ts = get_sysprice_list('2013-01-01 00:00:00', '2013-01-31 23:00:00', frequency='monthly')
print ts
'''with open('/home/martin/monthly_sys_prices.txt', 'a') as f:
    for i in range(0, len(times)):
        f.write(str(times[i]) + ' ' + str(prices[i]) + '\n')
    f.close()
print "All done"'''
#print datetime.date(datetime.datetim(2013,6,26,12,0).year, datetime.datetime(2013,6,26,12,0).month, 1)
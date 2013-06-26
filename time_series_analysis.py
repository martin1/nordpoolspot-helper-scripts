from data import *

start_date = '2011-01-01 01:00:00'
end_date = '2011-01-01 01:00:00'

buy_prices, buy_volumes, times = get_curve(start_date, end_date, type='buy', specified_hour = None)
sell_prices, sell_volumes, _ = get_curve(start_date, end_date, type='sell', specified_hour = None)

buy_prices1, buy_volumes1, times1 = get_data(start_date, end_date, type='buy', specified_hour = None)
sell_prices1, sell_volumes1, _ = get_data(start_date, end_date, type='sell', specified_hour = None)

with open('/home/martin/out.txt', 'w') as file:
    file.write(str(sell_volumes[0]) + "\n")
    file.write(str(sell_volumes1[0]))
    file.close()
    print "buy_volumes: " + str(buy_volumes[0] == buy_volumes1[0])
    print "buy_prices: " + str(buy_prices[0] == buy_prices1[0])
    print "sell_volumes: " + str(sell_volumes[0] == sell_volumes1[0])
    print "sell_prices: " + str(sell_prices[0] == sell_prices1[0])
    print "Done"
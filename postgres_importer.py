from data import *

start_date = '2013-01-01 00:00:00'
end_date = '2013-05-13 23:00:00'

def create_inserts(times, buy_volumes, buy_prices, sell_volumes, sell_prices, chart_data):
    queries = list()
    for n in range(0, len(times)):
        query = "insert into curve values('" + str(times[n]) + "'"
        for item in [buy_volumes[n], buy_prices[n], sell_volumes[n], sell_prices[n]]:
            query += ",'{"
            for i in range(0, len(item)):
                if i != 0:
                    query += ","
                query += str(item[i])
            query += "}'" + "\n" 
        for item in chart_data[n]:
            if isinstance(item, basestring):
                item = "'" + item + "'"
            query += "," + str(item)
        query += ");"
        #print query
        queries.append(query)
    return queries
        
def write_insert_sql(queries, filename="pg_insert_curves.sql"):
    with open(filename, "a") as file:
        for item in queries:
            file.write(item + "\n")
        file.close()
        print "Done" 
        
'''get data from MySQL database'''
'''buy_prices, buy_volumes, times = get_data(start_date, end_date, type='buy', specified_hour = None)
sell_prices, sell_volumes, _ = get_data(start_date, end_date, type='sell', specified_hour = None)
chart_data = get_chart_data(start_date, end_date)

write_insert_sql(create_inserts(times, buy_volumes, buy_prices, sell_volumes, sell_prices, chart_data))'''
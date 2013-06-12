import xlrd
import shutil
import os
import fnmatch
import datetime
from postgres_importer import *

    
def get_data(wb):
    times = list()
    buy_volumes = list()
    buy_prices = list()
    sell_volumes = list()
    sell_prices = list()
    chart_data = list()
    
    sh = wb.sheet_by_index(0)
    col=1
    while col <= sh.ncols:
        
        column_buy_volumes = list()
        column_buy_prices = list()
        column_sell_volumes = list()
        column_sell_prices = list()
        column_chart_data = list()
        '''get column time and chart data'''
        column_chart_data = list()
        for i in range(0,13):
            if i not in [6]: # skip unnecessary header rows
                if i == 0: # date needs to be converted
                    time = datetime.datetime.strptime(sh.cell_value(rowx=i, colx=col).replace(' +',''), "%d.%m.%Y %H:%M:%S")
                    time = datetime.datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
                    times.append(time)
                    continue
                column_chart_data.append(sh.cell_value(rowx=i,colx=col))
        #print column_chart_data
        
        '''get buy curve volume and price for column '''
        i=14
        while sh.cell_value(rowx=i,colx=col):
            if i%2==0:
                column_buy_prices.append(float(sh.cell_value(rowx=i,colx=col)))
            else:
                column_buy_volumes.append(sh.cell_value(rowx=i,colx=col))
            i+=1
        
        '''get sell curve volume and price for column '''
        i+=1
        while i < sh.nrows:
            if sh.cell_value(rowx=i, colx=col) is '':
                break
            if i%2==0:
                column_sell_volumes.append(sh.cell_value(rowx=i,colx=col))
            else:
                column_sell_prices.append(float(sh.cell_value(rowx=i,colx=col)))
            i+=1
            
        #sort column volumes and prices
        '''column_buy_volumes = sorted(column_buy_volumes, reverse=False)
        column_buy_prices = sorted(column_buy_prices, reverse=True)
        column_sell_volumes = sorted(column_sell_volumes, reverse=False)
        column_sell_prices = sorted(column_sell_prices, reverse=False)'''
        
        buy_volumes.append(sorted(column_buy_volumes, reverse=False))
        buy_prices.append(sorted(column_buy_prices, reverse=True))
        sell_volumes.append(sorted(column_sell_volumes, reverse=False))
        sell_prices.append(sorted(column_sell_prices, reverse=False))
        chart_data.append(column_chart_data)
        col+=2
        
    '''for item in sorted(buy_prices[0]):
        print item'''
    return times, buy_volumes, buy_prices, sell_volumes, sell_prices, chart_data

#################################################
'''paths for .xls files and generated csv files'''
xls_path = '/home/martin/dev/NordPool_data/'
sql_path = '/home/martin/dev/NordPool_data/'
processed_path = '/home/martin/dev/NordPool_data/processed/'
#count = 0

#################################################

times = list()
buy_volumes = list()
buy_prices = list()
sell_volumes = list()
sell_prices = list()
chart_data = list()



'''Check if we have any files to process'''
files = []
for file in os.listdir(xls_path):
    if fnmatch.fnmatch(file, '[MCP_Data_Report]*.xls'):
        files.append(xls_path + file)



if len(files) > 0:
    for file in files:
        print file
        wb = xlrd.open_workbook(file)
        file_times, file_buy_volumes, file_buy_prices, file_sell_volumes, file_sell_prices, file_chart_data = get_data(wb)
        #times += file_times
        #buy_volumes += file_buy_volumes
        #print len(buy_volumes)
        write_insert_sql(create_inserts(file_times, file_buy_volumes, file_buy_prices, file_sell_volumes, file_sell_prices, file_chart_data), 
                         sql_path + "pg_insert_curves.sql")
        '''buy_prices += file_buy_prices
        sell_volumes += file_sell_volumes
        sell_prices += file_sell_prices
        chart_data += file_chart_data'''
        print "Moving file.."
        shutil.move(file, processed_path)
       
print "Done"


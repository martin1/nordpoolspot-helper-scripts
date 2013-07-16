'''
Created on Feb 15, 2013

@author: martin
'''

import xlrd
import csv
import shutil
import os
import fnmatch
import datetime

    
def get_chart_data(wb, col=1):
    #wb = xlrd.open_workbook('/home/martin/dev/workspace/NordPoolSpot_DL/src/MCP_Data_Report_14-02-2013 00_00_00.xls')
    sh = wb.sheet_by_index(0)
    chart_data=[]
    for i in range(0,13):
        if i not in [6]: # skip unnecessary header rows
            if i == 0: # date needs to be converted
                date = datetime.datetime.strptime(sh.cell_value(rowx=i, colx=col).replace(' +',''), "%d.%m.%Y %H:%M:%S")
                date = datetime.datetime.strftime(date, '%Y-%m-%d %H:%M:%S')
                chart_data.append(date)
                continue
            chart_data.append(sh.cell_value(rowx=i,colx=col))
    return chart_data

    
#for item in headers:
#    print item
def get_data(wb, chart_time, col=1):
    
    '''get buy curve volume and price for column '''
    
    sh = wb.sheet_by_index(0)
    buy_volume=[]
    buy_price=[]
    i=14
    while sh.cell_value(rowx=i,colx=col):
        if i%2==0:
            buy_price.append(sh.cell_value(rowx=i,colx=col))
        else:
            buy_volume.append(sh.cell_value(rowx=i,colx=col))
        i+=1
    
    '''get sell curve volume and price for column '''
    sell_volume=[]
    sell_price=[]
    i+=1
    #while sh.cell_value(rowx=i,colx=col):
    while i < sh.nrows:
        if sh.cell_value(rowx=i, colx=col) is '':
            break
        if i%2==0:
            sell_volume.append(sh.cell_value(rowx=i,colx=col))
        else:
            sell_price.append(sh.cell_value(rowx=i,colx=col))
        i+=1
    
    '''compose results lists'''
    buy_curve_data = []
    sell_curve_data = []
    for i in range(0, len(buy_price)):
        buy_curve_data.append([chart_time] + [buy_price[i]] + [buy_volume[i]])
    
    for i in range(0, len(sell_price)):
        sell_curve_data.append([chart_time] + [sell_price[i]] + [sell_volume[i]])
        
    return buy_curve_data, sell_curve_data
    
def write_data(results, csv_out):
    with open(csv_out, 'ab') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in results:
            wr.writerow(item)
        csvfile.close()

def write_string(string, csv_out):
    with open(csv_out, 'ab') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        wr.writerow(string)
        csvfile.close()

        
#################################################
'''paths for .xls files and generated csv files'''
xls_path = '/home/martin/dev/NordPool_data/'
csv_path = '/home/martin/dev/NordPool_data/csv/'
processed_path = '/home/martin/dev/NordPool_data/processed/'
chart_data_file = 'chart_data.csv'
sell_price_volume_file = 'sell_price_volume.csv'
buy_price_volume_file = 'buy_price_volume.csv'
count = 0

#################################################

'''Check if we have any files to process'''
files = []
for file in os.listdir(xls_path):
    if fnmatch.fnmatch(file, '[MCP_Data_Report]*.xls'):
        files.append(xls_path + file)


if len(files) > 0:
    for file in files:
        print file
        wb = xlrd.open_workbook(file)
        sh = wb.sheet_by_index(0)
        '''Check if output files exist. Create templates if they do not exist'''
        if len(os.listdir(csv_path)) == 0:
            write_string(['time','currency','price_object_id','accepted_blocks_buy','accepted_blocks_sell'] + 
                         ['volume_net_flows','grid_scale_price','grid_scale_volume','min_price','max_price']+
                         ['min_volume','max_volume'], csv_path + chart_data_file)
            write_string(['time','price', 'volume'], csv_path + sell_price_volume_file)
            write_string(['time','price', 'volume'], csv_path + buy_price_volume_file)

        i = 1
        buy_curve_data = []
        sell_curve_data = []
        chart_data = []
        while i <= sh.ncols:
            buy_curve_data += get_data(wb, get_chart_data(wb, col=i)[0], col=i)[0]
            sell_curve_data += get_data(wb, get_chart_data(wb, col=i)[0], col=i)[1]
            chart_data.append(get_chart_data(wb, col=i))
            i+=2
        
            
        write_data(buy_curve_data, csv_path + buy_price_volume_file)
        write_data(sell_curve_data, csv_path + sell_price_volume_file)
        write_data(chart_data, csv_path + chart_data_file)
        
        shutil.move(file, processed_path)
        
        #count += 1
        #if count > 2:
        #    break
        
        

#write_data(get_data(wb, get_chart_data(wb, col=13), col=13), 'out.csv')
#get_chart_data(wb, col=47)





'''
Created on Feb 15, 2013

@author: martin
'''

import xlrd
import csv
from xlrd.sheet import empty_cell

#with open("MCP_Data_Report_14-02-2013 00_00_00.xls", "r") as f:
#    lines = f.readlines()
def get_headers(wb):    
    #wb = xlrd.open_workbook('/home/martin/dev/workspace/NordPoolSpot_DL/src/MCP_Data_Report_14-02-2013 00_00_00.xls')
    sh = wb.sheet_by_index(0)
    '''get headers and header data'''
    headers = []
    for i in range(0,16):
        headers.append(sh.cell_value(rowx=i,colx=0))
    headers.append('buy/sell')
    return headers
    
def get_header_data(wb, col=1):
    #wb = xlrd.open_workbook('/home/martin/dev/workspace/NordPoolSpot_DL/src/MCP_Data_Report_14-02-2013 00_00_00.xls')
    sh = wb.sheet_by_index(0)
    '''get headers and header data'''
    header_data=[]
    for i in range(0,16):
        header_data.append(sh.cell_value(rowx=i,colx=col))
    return header_data

    
#for item in headers:
#    print item
def get_data(wb, header_data, col=1):
    
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
    
    '''compose results list'''
    results = []
    for i in range(0, len(buy_price)):
        results.append([buy_price[i]] + [buy_volume[i]] + header_data + ['buy'])
    
    for i in range(0, len(sell_price)):
        results.append([sell_price[i]] + [sell_volume[i]] + header_data + ['sell'])
        
    return results
    
def write_data(results, csv_out):
    with open(csv_out, 'ab') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in results:
            wr.writerow(item)
        csvfile.close()

def write_headers(headers, csv_out):
    with open(csv_out, 'wb') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        wr.writerow(headers)
        csvfile.close()

        
#################################################
wb = xlrd.open_workbook('/home/martin/dev/workspace/NordPoolSpot_DL/src/MCP_Data_Report_14-02-2013 00_00_00.xls')
write_headers(get_headers(wb), 'out.csv')
i = 1
while i < 48:
    write_data(get_data(wb, get_header_data(wb, col=i), col=i), 'out.csv')
    i+=2


#write_data(get_data(wb, get_header_data(wb, col=13), col=13), 'out.csv')
#get_header_data(wb, col=47)





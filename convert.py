'''
Created on Feb 15, 2013

@author: martin
'''

import xlrd
import csv

#with open("MCP_Data_Report_14-02-2013 00_00_00.xls", "r") as f:
#    lines = f.readlines()
    
wb = xlrd.open_workbook('/home/martin/dev/workspace/NordPoolSpot_DL/src/MCP_Data_Report_14-02-2013 00_00_00.xls')
sh = wb.sheet_by_index(0)
#print sh.cell_value(rowx=0,colx=0)
'''get headers'''
headers = []
header_data=[]
for i in range(0,16):
    headers.append(sh.cell_value(rowx=i,colx=0))
    header_data.append(sh.cell_value(rowx=i,colx=1))
headers.append('buy_curve')
headers.append('sell_curve')

'''get header data'''
    
#for item in headers:
#    print item
'''get buy curve volume and price for column 1'''
buy_volume=[]
buy_price=[]
i=14
while sh.cell_value(rowx=i,colx=1):
    if i%2==0:
        buy_price.append(sh.cell_value(rowx=i,colx=1))
    else:
        buy_volume.append(sh.cell_value(rowx=i,colx=1))
    i+=1


'''get sell curve volume and price for column 1'''
sell_volume=[]
sell_price=[]
i+=1
while sh.cell_value(rowx=i,colx=1):
    if i%2==0:
        sell_volume.append(sh.cell_value(rowx=i,colx=1))
    else:
        sell_price.append(sh.cell_value(rowx=i,colx=1))
    i+=1

        
for item in sell_volume:
    print item


#your_csv_file = open('/home/martin/dev/workspace/NordPoolSpot_DL/src/output.csv', 'wb')
#wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

#for rownum in xrange(sh.nrows):
#    wr.writerow(sh.row_values(rownum))

#your_csv_file.close()
#print 'done'



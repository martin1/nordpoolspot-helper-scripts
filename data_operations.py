'''
Created on Feb 18, 2013

@author: martin
'''

''''ssh tunnel: ssh -N -p 1521 martin_kurgi@hektor1.ttu.ee -L 9990:127.0.0.1:3306'''

import MySQLdb
import matplotlib.pyplot as plt

con = MySQLdb.connect(host='127.0.0.1', user = 'martin_kurgi', passwd = '739503', db = 'martin_kurgi', port = 9990)
cur = con.cursor()  
cur.execute("select * from buy_price_volume where time = '2011-01-01 00:00:00'")
buy_rows = cur.fetchall()
cur.execute("select * from sell_price_volume where time = '2011-01-01 00:00:00'")
sell_rows = cur.fetchall()
con.close()


buy_prices = []
buy_volumes = []
sell_prices = []
sell_volumes = []

for item in buy_rows:
    buy_prices.append(item[1])
    buy_volumes.append(item[2])
    
for item in sell_rows:
    sell_prices.append(item[1])
    sell_volumes.append(item[2])
    

plt.plot(buy_volumes, buy_prices,'b-',sell_volumes, sell_prices, 'r-')
plt.show()


#for row in rows:
#    print row
#print len(rows)                                                                                                      

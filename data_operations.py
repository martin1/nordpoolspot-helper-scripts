'''
Created on Feb 18, 2013

@author: martin
'''

''''ssh tunnel: ssh -N -p 1521 martin_kurgi@hektor1.ttu.ee -L 9990:127.0.0.1:3306'''

import MySQLdb


db = MySQLdb.connect(host='127.0.0.1', user = 'martin_kurgi', passwd = '739503', db = 'martin_kurgi', port = 9990)
cur = db.cursor()  
cur.execute('select * from chart_data')

rows = cur.fetchall()

for row in rows:
    print row  
print len(rows)                                                                                                      

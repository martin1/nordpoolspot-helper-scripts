import urllib2
import datetime

fmt = "%d-%m-%Y"
url_start = "http://www.nordpoolspot.com/Global/Download%20Center%20Market%20Data/Market%20Cross%20Points%20data%20report/MCP_Data_Report_"
url_end = "%2000_00_00.xls"
latest = open('last.txt', 'r').read()

last_date = datetime.datetime.strptime(latest, fmt)

date = last_date + datetime.timedelta(days=1)
date = datetime.datetime.strftime(date, fmt)

print url_start + str(date) + url_end
u = urllib2.urlopen(url_start + str(date) + url_end)
with open("/home/martin/MCP_Data_Report_" + str(date) + " 00_00_00.xls", "w") as f:
    f.write(u.read())
    f.close()
    
with open("last.txt", "w") as f:
    f.write(date)
    f.close()



from data import *
from statsmodels.discrete.tests.results.results_discrete import cur_dir

volumes, prices, times = get_system_price_volume('2013-01-01 00:00:00', '2013-12-31 23:00:00')

con = psycopg2.connect(database="martin", user="postgres", password="postgres")
cur = con.cursor()

for i in range(0, len(times)):
    cur.execute("""UPDATE curve SET sys_volume = %s WHERE time = %s;""",
    (volumes[i], times[i]))
    print times[i]
con.commit()
con.close()
import pymysql
import pandas as pd
import csv
import os

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',password='root@lab3', db='stock_analysis')
c=conn.cursor()
table = 'stock_trade'
header = ['ts_code','trade_date', 'open','high','low', 'close','pre_close','pct_chg','vol', 'amount']
fpath = 'a_share.csv'
file = open(fpath)
cr = csv.reader(file, delimiter=',')
next(cr)


sqltemp = 'insert into {}({}) value({})'.format(table, ','.join(header), ('%s,'*len(header))[:-1])
for row in cr:  
    try:
        row = [None if r == '' else r for r in row]
        c.execute(sqltemp, row)
        print("inserting "+ str(row))
    except Exception as e:
        print(row)
        raise e
conn.commit()
file.close()

import pymysql
import pandas as pd
import csv
import os

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',password='root', db='stock_analysis')
c=conn.cursor()
table = 'stock_info'
header = ['ts_code','company_name', 'category']
fpath = 'stock_info.csv'
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
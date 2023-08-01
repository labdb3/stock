from db.connection import *


def get_open_price(start_date, end_date, code):
    sql = "SELECT * FROM stock_trade WHERE trade_date BETWEEN '{}' AND '{}' AND ts_code = '{}' order by trade_date asc".format(start_date,end_date,code)
    data = conn.execute(sql)
    data = [item[2] for item in data]
    return data



def get_stock_name():
    sql = "SELECT * FROM stock_info;"
    data = conn.execute(sql)
    return data


if __name__=='__main__':
    # get_stock_name()
    get_open_price("2020-01-01", "2023-07-05", "430047.BJ")

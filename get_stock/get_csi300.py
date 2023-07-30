import baostock as bs
import pymysql

def get_csi300_stocks():
    lg = bs.login()
    if lg.error_code != "0":
        raise Exception("登录失败：" + lg.error_msg)

    rs = bs.query_hs300_stocks()
    if rs.error_code != "0":
        bs.logout()
        raise Exception("获取沪深300股票列表失败：" + rs.error_msg)

    stocks = [d[1] for d in rs.data]
    bs.logout()

    prefix_stocks = []
    for stock_code in stocks:
        if stock_code.startswith("sh"):
            prefix_stocks.append(stock_code[3:] + ".SH")
        else:
            prefix_stocks.append(stock_code[3:] + ".SZ")

    return prefix_stocks

def get_csi500_stocks():
    lg = bs.login()
    if lg.error_code != "0":
        raise Exception("登录失败：" + lg.error_msg)

    rs = bs.query_zz500_stocks()
    if rs.error_code != "0":
        bs.logout()
        raise Exception("获取中证500股票列表失败：" + rs.error_msg)

    stocks = [d[1] for d in rs.data]
    bs.logout()

    prefix_stocks = []
    for stock_code in stocks:
        if stock_code.startswith("sh"):
            prefix_stocks.append(stock_code[3:] + ".SH")
        else:
            prefix_stocks.append(stock_code[3:] + ".SZ")

    return prefix_stocks


def update_stock_info(csi300_stocks, csi500_stocks):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root@lab3',
                                 db='stock_analysis')
    try:
        cursor = connection.cursor()
        for stock in csi300_stocks:
            update_csi_300 = f"UPDATE stock_info set is_csi_300 = true where ts_code ='{stock}'"
            cursor.execute(update_csi_300)
        for stock in csi500_stocks:
            update_csi_500 = f"UPDATE stock_info set is_csi_500 = true where ts_code ='{stock}'"
            cursor.execute(update_csi_500)

    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))
    finally:
        cursor.close()
        connection.commit()
        connection.close()

csi300_stocks = get_csi300_stocks()
csi500_stocks = get_csi500_stocks()

update_stock_info(csi300_stocks= csi300_stocks, csi500_stocks= csi500_stocks)
from Alpha_code_1 import *
import pymysql


def get_csi300_stock(start_date ='2020-01-01',end_date='2023-07-05'):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root@lab3',
                                 db='stock_analysis')
    try:
        cursor = connection.cursor()
        sql = "select stock_trade.* from stock_trade join stock_info on stock_trade.ts_code = stock_info.ts_code and stock_info.is_csi_300 = true and trade_date between %s and %s order by ts_code asc, trade_date asc;"
        cursor.execute(sql, (start_date, end_date))
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        return df
    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        connection.close()


def get_csi500_stock(start_date ='2020-01-01',end_date='2023-07-05'):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root@lab3',
                                 db='stock_analysis')
    try:
        cursor = connection.cursor()
        sql = "select stock_trade.* from stock_trade join stock_info on stock_trade.ts_code = stock_info.ts_code and stock_info.is_csi_500 = true and trade_date between %s and %s order by ts_code asc, trade_date asc;"
        cursor.execute(sql, (start_date, end_date))
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        return df
    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        connection.close()


def get_stock_with_sector(sector_name, start_date = '2020-01-01', end_date = '2023-07-05'):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root@lab3',
                                 db='stock_analysis')
    try:
        cursor = connection.cursor()
        sql = "select stock_trade.* from stock_trade join stock_info on stock_trade.ts_code = stock_info.ts_code and stock_info.category = %s and trade_date between %s and %s order by ts_code asc, trade_date asc;"
        cursor.execute(sql, (sector_name, start_date, end_date))
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        return df
    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        connection.close()


def get_stock_with_code(start_date='2020-01-01', end_date='2023-07-05', code_list = None):
    # 连接数据库
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root@lab3',
                                 db='stock_analysis')
    try:
        cursor = connection.cursor()
        if code_list is not None:
            sql = "SELECT * FROM stock_trade WHERE trade_date BETWEEN %s AND %s AND ts_code IN ({}) ORDER BY ts_code asc, trade_date ASC".format(','.join(['%s'] * len(code_list)))
            parameters = [start_date, end_date] + code_list
            cursor.execute(sql,parameters)
        else:
            sql = "SELECT * FROM stock_trade WHERE trade_date BETWEEN %s AND %s order by ts_code asc ,trade_date asc"
            cursor.execute(sql, (start_date, end_date))
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])

        return df

    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        connection.close()

##demo_result = get_csi300_stock("2023-05-10","2023-07-05")
##demo_result = get_csi500_stock("2023-05-10","2023-07-05")

demo_result = get_stock_with_sector("软件开发","2023-01-10","2023-07-05")

another_alpha = get_alpha(demo_result)
'''
demo_result['alpha001'] = another_alpha['alpha001']
demo_result['alpha002'] = another_alpha['alpha002']
demo_result['alpha003'] = another_alpha['alpha003']
demo_result['alpha003'] = another_alpha['alpha003']
demo_result['alpha004'] = another_alpha['alpha004']
demo_result['alpha005'] = another_alpha['alpha005']
demo_result['alpha006'] = another_alpha['alpha006']
'''
demo_result['alpha007'] = another_alpha['alpha007']
demo_result['alpha008'] = another_alpha['alpha008']
##demo_result.to_csv("a.csv")
print(demo_result)




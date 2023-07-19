from Alpha_code_1 import *
import pymysql

def get_stock(start_date, end_date, code):
    # 连接数据库
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root@lab3',
                                 db='stock_analysis')
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行 SQL 查询
        sql = "SELECT * FROM stock_trade WHERE trade_date BETWEEN %s AND %s AND ts_code = %s order by trade_date asc"
        cursor.execute(sql, (start_date, end_date, code))

        # 获取查询结果
        results = cursor.fetchall()

        # 将结果转换为 DataFrame 格式
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])

        return df

    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        connection.close()


demo_result = get_stock("2020-01-01","2023-07-05","430047.BJ")
another_alpha = get_alpha(demo_result)
print(another_alpha['alpha012'])


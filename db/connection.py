import pymysql
import pandas as pd
import pickle
import matplotlib.pyplot as plt

class Connection:
    def __init__(self):
        self.conn = pymysql.connect(host='10.129.167.169',
                                     port=3306,
                                     user='root',
                                     password='root@lab3',
                                     db='stock_analysis')
        self.cursor = self.conn.cursor()

    def execute(self,sql):
        # 执行 SQL 查询
        self.cursor.execute(sql)

        # 获取查询结果
        results = self.cursor.fetchall()

        # 将结果转换为 DataFrame 格式
        df = pd.DataFrame(results, columns=[desc[0]
                                            for desc in self.cursor.description])

        return [item for item in df.values.tolist()]
    def close(self):
        self.cursor.close()
        self.connection.close()


conn = Connection()

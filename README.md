# stock

## 数据初始化教程(可以在本地部署该项目)
a_share.csv文件过大，超出了github单个文件的大小限制，我是手动传到服务器上的。可以'scp fcg@10.129.167.169:/home/fcg/stock/a_share.csv /your_diectory' 传输到本地
1. 运行table_create.sql中的sql语句。
2. 运行import_stock_info.py，注意修改其中的mysql账号密码信息。
3. 运行import_stock_info.py,注意修改其中的mysql账号密码信息。
4. 删除stock_trade中东方财富无法获取行情信息和已经退市的股票
'''
delete from stock_trade where ts_code like '%.BJ';
delete from stock_trade where ts_code='002417.SZ';
delete from stock_trade where ts_code='688555.SH';
delete from stock_trade where ts_code='688086.SH';
'''

### 如何使用因子库
服务器IP 10.129.167.169 服务器密码：fcg@lab3 端口：22 项目目录：/home/fcg/stock

mysql数据库用户名: root 
mysql数据库密码: root@lab3
mysql数据库名称: stock_analysis 
mysql表名：stock_trade 股票交易信息 stock_info 股票基本信息
#### 因子库使用方式：
因子的计算公式: 具体计算公式我已经在代码注释中给出，在Alpha_code_1.py文件中，在现阶段，请不要使用带有rank, ts_rank的因子进行计算。
因子计算相关API
```python
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
```

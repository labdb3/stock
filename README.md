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
5. 运行get_csi300.py,添加沪深300和中证500指数的相关信息。

### 板块信息列表
|银行               |
| 房地产开发         |
| 软件开发           |
| 环保行业           |
| 房地产服务         |
| 交运设备           |
| 综合行业           |
| 工程建设           |
| 玻璃玻纤           |
| 家电行业           |
| 贸易行业           |
| 光学光电子         |
| 消费电子           |
| 水泥建材           |
| 汽车服务           |
| 珠宝首饰           |
| 电力行业           |
| 医药商业           |
| 汽车零部件         |
| 通信设备           |
| 计算机设备         |
| 文化传媒           |
| 通用设备           |
| 多元金融           |
| 电池               |
| 装修装饰           |
| 商业百货           |
| 石油行业           |
| 有色金属           |
| 电子元件           |
| 航运港口           |
| 航空机场           |
| 化学制药           |
| 工程机械           |
| 证券               |
| 化纤行业           |
| 电网设备           |
| 生物制品           |
| 燃气               |
| 化肥行业           |
| 互联网服务         |
| 化学原料           |
| 中药               |
| 旅游酒店           |
| 铁路公路           |
| 造纸印刷           |
| 医疗服务           |
| 农牧饲渔           |
| 贵金属             |
| 专用设备           |
| 食品饮料           |
| 农药兽药           |
| 教育               |
| 公用事业           |
| 汽车整车           |
| 煤炭行业           |
| 物流行业           |
| 化学制品           |
| 酿酒行业           |
| 橡胶制品           |
| 美容护理           |
| 装修建材           |
| 保险               |
| 钢铁行业           |
| 小金属             |
| 包装材料           |
| 医疗器械           |
| 半导体             |
| 航天航空           |
| 纺织服装           |
| 能源金属           |
| 工程咨询服务       |
| 塑料制品           |
| 通信服务           |
| 电机               |
| 家用轻工           |
| 仪器仪表           |
| 光伏设备           |
| 非金属材料         |
| 游戏               |
| 风电设备           |
| 采掘行业           |
| 电源设备           |
| 专业服务           |
| 电子化学品         |
| 船舶制造           |

### 如何使用因子库
服务器IP 10.129.167.169 服务器密码：fcg@lab3 端口：22 项目目录：/home/fcg/stock

mysql数据库用户名: root 
mysql数据库密码: root@lab3
mysql数据库名称: stock_analysis 
mysql表名：stock_trade 股票交易信息 stock_info 股票基本信息
#### 因子库使用方式：
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

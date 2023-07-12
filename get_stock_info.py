import requests
import pymysql
from bs4 import BeautifulSoup
import pandas as pd

def get_stock_sector(stock_code):
    url = f"http://quote.eastmoney.com/{stock_code}.html"  # 构建股票详情页的URL
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}  # 设置请求头，模拟浏览器访问
    response = requests.get(url, headers=headers, allow_redirects=True)
    ##print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    ##print(soup.select(".breadcrumb_item")[3].text)
    sector = soup.select(".breadcrumb_item")[2].text
    company_name = soup.select(".breadcrumb_item")[3].text
    return sector,company_name


def get_stock_list():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='stock_analysis')

    try:
        cursor = connection.cursor()

        # 执行 SQL 查询
        sql = "SELECT distinct ts_code FROM stock"
        cursor.execute(sql)

        # 获取查询结果
        results = cursor.fetchall()
        results_list = []
        for re in results:
            results_list.append(re[0])
        return results_list

    except Exception as e:
        print("Error occurred while fetching data from database:", str(e))

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        connection.close()


def convert_stock_code_list(origin_list):
    res = []
    for stock_code in origin_list:
        prefix = stock_code[-2:].lower()
        code = stock_code[:-3]
        if prefix == 'sh' or prefix == 'sz' or prefix == 'bj':
            res.append(prefix + code)
    return res



def reverse_convert_stock_code(code):
    prefix = code[0:2].upper()
    code_num = code[2:]
    return code_num +"."+ prefix

get_stock_sector("sh688001")
demo = get_stock_list()
a_stock_list = convert_stock_code_list(demo)  # 示例股票代码列表
data = []
df = pd.DataFrame()

for stock_code in a_stock_list:
    try:
        sector,company_name = get_stock_sector(stock_code)
        data ={'ts_code': [reverse_convert_stock_code(stock_code)],'company_name':[company_name],'sector':[sector]}
        new_row = pd.DataFrame(data)
        df = pd.concat([df, new_row], axis=0) 
        ##print(df)
    except Exception as e:
        print("exception "+ str(e) + " in" + stock_code)
        ##print(str(e))
print(len(df))
df.to_csv("stock_info.csv",index = False)
print(df)
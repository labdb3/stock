import pymysql
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from commons.utils import *
from commons.plot_figure import *
from corr import *


# stocks = get_stock_name()
#
# category = {}
# for item in stocks:
#     if item[2] not in category:
#         category[item[2]]=[item[:2]]
#     else:
#         category[item[2]].append(item[:2])
#
# stock_op = {}
# print(category['软件开发'])
# print(len(category['软件开发']))
#
# for stock in category["软件开发"]:
#     print(stock)
#     open_price = get_open_price("2023-03-01", "2023-05-30", stock[0])
#     stock_op[stock[0]]=open_price
#

# pickle.dump(stock_op,open("data.pkl","wb"))
read_data = pickle.load(open("data.pkl","rb"))
data = []
for k,v in read_data.items():
    print(len(v))
    if len(v)!=122: continue
    data.append(v)
print(len(data))
get_graph(data)

# names,corr = get_corr(data)
# plot_f(names,corr)


import pymysql
import pandas as pd
import pickle
import matplotlib.pyplot as plt


def plot_f(names,corr):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(names)
    ax.set_xticks(range(len(names)))
    ax.set_yticklabels(names)
    ax.set_yticks(range(len(names)))
    im = ax.imshow(corr, cmap=plt.cm.hot_r)
    # 添加颜色刻度条
    plt.colorbar(im)
    # 添加中文标题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("coor")
    plt.xlabel('code')
    plt.ylabel('code')
    plt.show()
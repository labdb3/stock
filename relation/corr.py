import pymysql
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import networkx as nx

def get_corr(data):
    stockCloseDF = pd.DataFrame()
    for i in range(len(data)):
        stockCloseDF[i] = data[i]


    stockname = [str(i) for i in range(len(data))]
    return stockname,stockCloseDF.corr()

def get_graph(data):
    names, corr = get_corr(data)
    corr = corr.to_numpy().tolist()

    G = nx.Graph()
    for i in range(len(data)):
        for j in range(len(data)):
            G.add_edge(i,j,weight = corr[i][j])

    node_size = []
    node_list =list(G.nodes())
    for i in node_list:
        size = abs(sum(corr[i]))
        node_size.append(size)

    # print(node_size)

    edges = [(u,v,d) for (u,v,d) in G.edges(data=True) if d['weight']>0.5]
    edges_size = [list(d.values())[0] for (u,v,d) in G.edges(data=True) if d['weight']>0.5]
    print(edges_size)
    # print(edges)
    pos = nx.spring_layout(G)
    print(len(edges),len(edges_size))
    nx.draw_networkx_nodes(G, pos, alpha=0.6, nodelist=node_list,node_size=node_size)
    # # edge
    nx.draw_networkx_edges(G, pos, edgelist=edges,width=edges_size, alpha=0.6)
    # # label
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.axis('off')
    plt.title('红楼梦社交网络')
    plt.show()



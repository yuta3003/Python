import binascii
import dpkt
import matplotlib.pyplot as plt
import networkx as nx
import os
import socket
import string
import sys

"""
python pcap.py <ファイル名>
ファイルの保存形式
    Wireshark/tcpdump/...   .pcap

pip install dpkt
pip install networkx
pip install matplotlib
"""

def main(file_name):
    """
    main関数

    Parameters
    ----------
    file_name : string
        対象のファイル名

    Returns
    -------
    """
    packet_count = 0
    pcr = dpkt.pcap.Reader(open(file_name,'rb'))

    #パケット処理
    for ts,buf in pcr:
        packet_count += 1
        try:
            eth = dpkt.ethernet.Ethernet(buf)
        except:
            continue

        #IPデータの場合
        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            with open('./edgelist.txt', 'a') as f:
                print("{} {}".format(src, dst), file = f)
    
    input("進みます")
    G = nx.read_edgelist('edgelist.txt', nodetype=str)  # ファイル読み込み
    plt.figure(figsize=(7, 7))
    pos = nx.spring_layout(G)

    #PageRankの追加
    pr = nx.pagerank(G)
    nx.draw_networkx_edges(G, pos, edge_color='y')

    #node_sizeにPageRankの値を組み込む
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color='r',
        alpha=0.5,
        node_size=[5000*v for v in pr.values()]
    )
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10
    )

    plt.axis('off')
    plt.show()

    os.remove("edgelist.txt")
    print("処理終了:{}".format(packet_count))

#メイン関数
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("ファイルを指定して下さい")
        exit()
    #第2引数をファイル名にする
    file_name = sys.argv[1]

    main(file_name)
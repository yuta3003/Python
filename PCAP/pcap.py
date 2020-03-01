import dpkt, socket
import string
import binascii
import sys

"""
python pcap.py <ファイル名>
ファイルの保存形式
    Wireshark/tcpdump/...   .pcap

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
            packet_analysis(eth)
        except:
            continue

    print("処理終了:{}件".format(packet_count))


def packet_analysis(ipinfo):
    #IPデータの場合
    if type(ipinfo.data) == dpkt.ip.IP:
        ip = ipinfo.data
        ipheader(ip)

        #TCPデータ
        if type(ip.data) == dpkt.tcp.TCP:
            tcp = ip.data
            if len(tcp.data) != 0:  #ペイロードが0以外
                thex = binascii.b2a_hex(tcp.data)
                payload(thex)
        #UDPデータ
        elif type(ip.data) == dpkt.udp.UDP:
            udp = ip.data
            if len(udp.data) != 0:  #ペイロードが0以外
                uhex = binascii.b2a_hex(udp.data)
                payload(uhex)
        #ICMPデータ
        elif type(ip.data) == dpkt.icmp.ICMP:
            icmp = ip.data
            if len(icmp.data) != 0: #ペイロードが0以外
                ihex = binascii.hexlify(str(icmp.data))
                payload(ihex[8:])


#IPヘッダ処理
def ipheader(header):
    """
    IP Header情報を表示する

    Parameters
    ----------
    header : dpkt.ethernet.Ethernet
        ペイロードのHeader情報
    """
    #ヘッダの処理
    src = socket.inet_ntoa(header.src)
    dst = socket.inet_ntoa(header.dst)
    if type(header.data) == dpkt.tcp.TCP:       #TCP
        print("TCP {}:{} => {}:{} (len:{})".format(
            src,
            header.data.sport,
            dst,
            header.data.dport,
            len(header.data.data)
        ))
    elif type(header.data) == dpkt.udp.UDP:     #UDP
        print("UDP {}:{} => {}:{} (len:{})".format(
            src,
            header.data.sport,
            dst,
            header.data.dport,
            len(header.data.data)
        ))
    elif type(header.data) == dpkt.icmp.ICMP:   #ICMP
        print("ICMP {}:type {},code {} => {} (len:{})".format(
            src,
            header.data.type,
            header.data.code,
            dst,
            len(header.data.data)
        ))
        
    #その他
    else:
        print("{} => {}".format(src, dst))
        return


#ペイロード
def payload(thex):
    #ペイロードの処理
    return


#メイン関数
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("ファイルを指定して下さい")
        exit()
    #第2引数をファイル名にする
    file_name = sys.argv[1]

    main(file_name)
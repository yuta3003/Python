import socket
"""
TCP クライアントを実装
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 50000
server = (ip, port)

sock.connect(server)

msg = ''
while msg != 'exit':
    # データ送信
    msg = input('-> ')      # 標準入力からデータを取得
    msg_binary = msg.encode()
    sock.send(msg_binary) # サーバにデータを送信

    # データ受信
    data_binary = sock.recv(1024)  # サーバからデータを受信　byte=1024
    data = data_binary.decode
    print('Received from server:{}'.format(data))   # 受信したデータを表示

sock.close()

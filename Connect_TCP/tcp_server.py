import socket
"""
TCP Echoサーバを実装
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '127.0.0.1'
port = 50000
host = (host_ip, port)

sock.bind(host)
sock.listen(1)  # 接続するクライアントを指定

print("Waiting connection ...")

connection, addr = sock.accept()
print("Connection from:{}".format(addr))

while True:
    # 受信部
    data_binary = connection.recv(1024)    # クライアントからデータを受信
    data = data_binary.decode()
    if data == 'exit':             # dataはバイト列のため b'exit'
        break
    print('Received a message:{}'.format(data))

    # 送信部
    connection.send(data_binary)
    print("Sent a message:{}".format(data))

# 後処理
connection.close()
sock.close()
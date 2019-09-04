import socket

# 建立连接，指明类型和协议
# AF_INET = 2 IPv4
# AF_INET6 = 23 IPv6
# 注意 server 和 client 为固定写法
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 所有ip均可访问
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

# 获取从客户端发送的数据
data = sock.recv(1024)
print(data.decode("utf8"))

# server发送数据
sock.send("hello, {}".format(data.decode("utf8")).encode("utf8"))
sock.send("hello".encode("utf8"))

sock.close()
server.close()

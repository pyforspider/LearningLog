import socket

# 建立连接，指明类型和协议
# AF_INET = 2 IPv4
# AF_INET6 = 23 IPv6
clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接ip地址为xxx的服务器, 服务器是本地，所以 127.0.0.1
clint.connect(('127.0.0.1', 8000))

# 客户发送数据
clint.send("bobby".encode("utf8"))

# 客户接收数据, 服务端发送一次，客户端接收一次
data = clint.recv(1024)
print(data.decode("utf8"))
data = clint.recv(1024)
print(data.decode("utf8"))

clint.close()

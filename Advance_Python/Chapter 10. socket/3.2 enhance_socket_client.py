# 实现用户即时聊天
import socket

# 建立连接，指明类型和协议
clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接ip地址为xxx的服务器, 服务器是本地，所以 127.0.0.1
clint.connect(('127.0.0.1', 8000))

while True:
	re_data = input()
	if re_data == "exit":
		break
	clint.send(re_data.encode("utf8"))

	data = clint.recv(1024)
	print(data.decode("utf8"))

clint.close()

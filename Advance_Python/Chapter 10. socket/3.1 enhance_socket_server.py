# 实现用户即时聊天
import socket

# 建立连接，指明类型和协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 所有ip均可访问
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

while True:
	# 获取从客户端发送的数据
	data = sock.recv(1024)
	print(data.decode("utf8"))

	# server发送数据
	re_data = input()
	sock.send(re_data.encode("utf8"))

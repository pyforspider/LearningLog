# 实现多用户聊天, 使用多线程来实现
import socket
import threading

# 建立连接，指明类型和协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 所有ip均可访问
server.bind(('0.0.0.0', 8000))
server.listen()


def handel_sock(sock, addr):
	while True:
		# 获取从客户端发送的数据
		data = sock.recv(1024)
		print(data.decode("utf8"))
		if data.decode("utf8") == "exit":
			break
		# server发送数据
		re_data = input()
		sock.send(re_data.encode("utf8"))
	sock.close()


while True:
	sock, addr = server.accept()
	thread = threading.Thread(target=handel_sock, args=(sock, addr))
	# 线程 start() 方法开启线程
	thread.start()

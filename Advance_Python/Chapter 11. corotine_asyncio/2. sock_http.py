# requests -> urllib -> socket
import socket
from urllib.parse import urlparse


def get_url(url):
	url = urlparse(url)
	path = url.path
	host = url.netloc
	if path == "":
		path = "/"

	# client 为固定写法
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.setblocking(False)
	client.connect((host, 80))

	# http 的 send() 方法固定写法：
	client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

	data = b""
	while True:
		d = client.recv(1024)
		if d:
			data += d
		else:
			break
	client.close()
	return data.decode("utf-8").split("\r\n\r\n")[1]


if __name__ == '__main__':
	html = get_url("http://www.baidu.com")
	print(html)

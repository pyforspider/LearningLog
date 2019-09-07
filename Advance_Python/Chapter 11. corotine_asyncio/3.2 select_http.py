# 1. epoll并不一定比 select好
# 2. 在并发度高，连接不活跃时，epoll好， 如 网页
# 3. 在连接活跃，并发度不高时， select好， 如 游戏

import socket
import time
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = []
stop = False
# user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"


# 通过select实现http请求
class Fetcher:
	# 为什么使用类？ 为了共享变量!
	def connected(self, key):
		selector.unregister(key.fd)
		self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
		selector.register(self.client.fileno(), EVENT_READ, self.get_data)

	# 如果数据准备好了，事件循环会不断执行这个函数, 直到else取消register
	def get_data(self, key):
		d = self.client.recv(1024)
		if d:
			self.data += d
		else:
			print(self.data.decode("utf-8").split("\r\n\r\n")[1])
			selector.unregister(key.fd)
			self.client.close()
			urls.remove(self.spider_url)
			if not urls:
				global stop
				stop = True

	def get_url(self, url):
		self.spider_url = url
		url = urlparse(url)
		self.path = url.path
		self.host = url.netloc
		if self.path == "":
			self.path = "/"
		self.data = b""

		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.setblocking(False)
		try:
			self.client.connect((self.host, 80))
		except BlockingIOError:
			pass

		# 注册
		selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
	# 事件循环，不停的请求socket的状态并调用对应的回调函数
	# 1. select 本身不支持register模式
	# 2. socket 状态变化以后的回调由程序员完成
	# SelectorKey = namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])
	while not stop:
		ready = selector.select()
		for key, mask in ready:
			# key: SelectorKey(fileobj=372, fd=372, events=2, data=<bound method Fetcher.connected of <__main__.Fetcher object at 0x00000000029EFE48>>)
			# mask: 2
			call_back = key.data    # key.fd
			call_back(key)
	# 回调+事件循环+ select(poll\epoll)


if __name__ == '__main__':
	start_time = time.time()
	for i in range(20):
		url = "http://shop.projectsedu.com/goods/{}/".format(i)
		urls.append(url)
		fetcher = Fetcher()
		fetcher.get_url(url)
	loop()
	print("last time: {}".format(time.time()-start_time))

	# 标准运行
	# url = "http://www.baidu.com"
	# urls.append(url)
	# fetcher = Fetcher()
	# fetcher.get_url(url)
	# loop()

	# 以下 url 不知名原因 301 无法爬取
	# url = "https://pubs.acs.org/action/doSearch?AllField=BODIPY&pageSize=20&startPage=1"
	# url = "https://pubs.acs.org/doi/10.1021/am506262u"
	# url = "https://new.qq.com/ch/world/"

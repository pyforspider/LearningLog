# 事件循环+回调(驱动生成器) + epoll (IO多路复用）
# asyncio 是python用于解决一步io编程的一整套方案
# tornado、 gevent、 twisted (scrapy, django_channels) 都是由 asyncio 实现的
# tornado (实现web服务器高并发)， django+flask（uwsgi， gunicorn + nginx）
# tornado 可以直接部署， nginx + tornado

# 使用asyncio
import asyncio
import time


async def get_html(url):
	print("start get url")
	# await time.sleep(2)    # NoneType can't be used in 'await' expression
	# time.sleep(2)          # 阻塞io不要写在协程
	await asyncio.sleep(2)   # 返回一个further
	print("end get url")


if __name__ == "__main__":
	# start_time = time.time()
	# loop = asyncio.get_event_loop()
	# loop.run_until_complete(get_html("http://www.imooc.com"))
	# print("last time: {}".format(time.time()-start_time))

	start_time = time.time()
	loop = asyncio.get_event_loop()
	tasks = [get_html("http://www.imooc.com") for i in range(10)]
	# loop.run_until_complete 可以接收 1. 协程函数 2. asyncio.wait( 打包的协程函数 -> tasks) asyncio.wait() 接收一个可迭代对象
	loop.run_until_complete(asyncio.wait(tasks))
	print("last time: {}".format(time.time()-start_time))

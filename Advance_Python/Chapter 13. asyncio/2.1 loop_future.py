# 获取协程的返回值

import asyncio
import time
from functools import partial


async def get_html(url):
	print("start get url")
	await asyncio.sleep(2)   # 返回一个future
	# print("end get url")
	return "bobby"


# callback 被传递了一个参数 future/task
def callback(url, future):
	print(url, future)
	print("send email to bobby")


if __name__ == "__main__":
	loop = asyncio.get_event_loop()

	# 两种方法获取 future:  task 是 future 的子类
	# future = asyncio.ensure_future(get_html("http://www.imooc.com"))
	task = loop.create_task(get_html("http://www.imooc.com"))

	# 增加回调函数, partial()可以给函数增加一个绑定的参数
	# task.add_done_callback(callback)
	task.add_done_callback(partial(callback, "http://www.imooc.com"))

	# loop.run_until_complete() 可以接收 1.future/task类型, 2.协程函数类型， 3.asyncio.wait(打包函数)类型, 即协程类型
	# loop.run_until_complete(future)
	loop.run_until_complete(task)

	# future.result() 获取结果
	# print(future.result())
	print(task.result())

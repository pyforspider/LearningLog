# wait和gather的区别

import asyncio
import time


async def get_html(url):
	print("start get url")
	await asyncio.sleep(2)   # 返回一个future
	print("end get url")


if __name__ == "__main__":
	start_time = time.time()
	loop = asyncio.get_event_loop()
	tasks = [get_html("http://www.imooc.com") for i in range(10)]
	# loop.run_until_complete(asyncio.wait(tasks))
	# loop.run_until_complete(asyncio.gather(*tasks))
	# print("last time: {}".format(time.time()-start_time))

	# gather和wait的区别
	# gather更加 high-level
	group1 = [get_html("http://projectsedu.com") for i in range(2)]
	group2 = [get_html("http://www.imooc.com") for i in range(2)]
	# loop.run_until_complete(asyncio.gather(*group1, *group2))
	# print("last time: {}".format(time.time()-start_time))

	# gather 另外用法
	group1 = asyncio.gather(*group1)
	group2 = asyncio.gather(*group2)
	group2.cancel()
	loop.run_until_complete(asyncio.gather(group1, group2))
	print("last time: {}".format(time.time()-start_time))

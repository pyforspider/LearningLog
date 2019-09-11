# asyncio 同步和通信, 需要锁的情况
# 方法1：                            方法2：                  方法3：
# await lock.acquire()              with await lock:         async with lock:
# lock.release()


import asyncio
from asyncio import Lock, Queue
import aiohttp

cache = {}
lock = Lock()


# 当有两个或两个以上任务需要调用此协程，获取相同url返回的结果时，如果缓存cache中没有结果时，可能造成这两个任务都调用 await
# 而实际只需要获取一次，如果不加锁会造成多次调用，降低效率
# 加锁方式： async with lock:
async def get_stuff(url):
	async with lock:
		if url in cache:
			return cache[url]
		stuff = await aiohttp.request('GET', url)
		cache[url] = stuff
		return stuff


# 此协程任务需要调用 get_stuff()
async def parse_stuff():
	stuff = await get_stuff()
	# do some parsing


# 此协程任务也需要调用 get_stuff()
async def use_stuff():
	stuff = await get_stuff()
	# use stuff to sth. interesting


tasks = [parse_stuff(), use_stuff()]

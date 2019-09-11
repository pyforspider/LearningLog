# asyncio 同步和通信, 协程里的[同步操作]不需要锁，就可以使结果为0

import asyncio

total = 0


async def add():
	# 1. do sth.
	# 2. io操作
	# 3. do sth.
	global total
	for i in range(100000):
		total += 1


async def desc():
	global total
	for i in range(100000):
		total -= 1


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [add(), desc()]
	loop.run_until_complete(asyncio.wait(tasks))
	print(total)

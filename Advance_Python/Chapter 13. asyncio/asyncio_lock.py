import asyncio

total = 0


async def add():
	# 1 dosomthing1
	# 2 io操作
	# 1. dosomething3
	global total
	for i in range(100000):
		total += 1


async def desc():
	global total
	for i in range(100000):
		total -= 1


if __name__ == '__main__':
	tasks = [add(), desc()]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))
	print(total)

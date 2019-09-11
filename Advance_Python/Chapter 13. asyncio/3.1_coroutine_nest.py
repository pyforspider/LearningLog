# 1. loop.run_until_complete & loop.run_forever()
# 2. 取消task任务
import asyncio

# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

# 1. loop会被放到future中
# 2. 取消future(task)


async def get_html(sleep_time):
	print("waiting")
	await asyncio.sleep(sleep_time)
	print("done after {}s".format(sleep_time))


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	task1 = get_html(1)
	task2 = get_html(2)
	task3 = get_html(3)
	tasks = [task1, task2, task3]
	try:
		loop.run_until_complete(asyncio.wait(tasks))
	except KeyboardInterrupt:
		# 取消任务
		all_tasks = asyncio.Task.all_tasks()
		for task in all_tasks:
			print("cancel task: ", task.cancel())
		# 直接 loop.close()会报错，需要先 stop(), run_forever(), 最后close()
		loop.stop()
		# stop()后 需要重启loop.run_forever()
		loop.run_forever()
	finally:
		loop.close()

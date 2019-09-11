# loop.call_soon(func_name, func_args)
# loop.call_soon_threadsafe(func_name, func_args)

# loop.call_later(wait_time, func_name, func_args)

# loop.call_at(loop.time()+wait_time, func_name, func_args)


import asyncio


def call_back(sleep_time):
	print("sleep {} success".format(sleep_time))
	print(loop.time())


def stop_loop(loop):
	loop.stop()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	# call_soon(func_name, func_args)
	# loop.call_soon(call_back, 2)
	# loop.call_soon(stop_loop, loop)
	# call_later(wait_time, func_name, func_args)
	now = loop.time()
	loop.call_soon(call_back, 0.5)
	loop.call_at(now+1, call_back, 1)
	loop.call_at(now+2, call_back, 2)
	loop.call_at(now+3, call_back, 3)
	loop.call_later(5, stop_loop, loop)
	loop.run_forever()

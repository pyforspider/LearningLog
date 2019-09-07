# 生成器的send()方法


def gen_func():
	# 1. 可以产出值，2. 可以接收值(调用方传递进来的值)
	html = yield "http://projectsedu.com"
	print(html)
	yield 2
	yield 3
	return "bobby"


# 生成器不只可以产出值，还可以接收值


if __name__ == "__main__":
	gen = gen_func()
	# 在调用send()发送非None值之前，必须先启动一次生成器. 方法1：next(gen) 方法2： gen.send(None)
	print(next(gen))  # 等同于 gen.send(None)
	# send() 方法向 yield 传值，并执行下一个 yield 语句
	print(gen.send("bobby"))
	print(next(gen))
	try:
		next(gen)
	except StopIteration as e:
		print(e.value)

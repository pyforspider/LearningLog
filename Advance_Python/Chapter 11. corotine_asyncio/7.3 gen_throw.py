# 生成器的throw()方法, 1. 扔出异常 2. 执行gen到下一个yield


def gen_func():
	try:
		yield "http://projectsedu.com"
	except Exception:
		pass
	yield 2
	try:
		yield 3
	except Exception:
		pass
	return "bobby"


if __name__ == "__main__":
	gen = gen_func()
	print(next(gen))                          # yield "http://projectsedu.com"
	# 1. throw() 方法会在 执行完的 yield 语句抛出 throw 扔出的异常, 需要自己在 生成器 处理
	# 2. throw() 方法和send() 一样都会, 执行下一个 yield 语句
	gen.throw(Exception, "download error")    # yield 2
	print(next(gen))                          # yield 3
	try:
		gen.throw(Exception, "download error")
	except StopIteration as e:
		print(e.value)

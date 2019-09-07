# 生成器的close()方法


def gen_func():
	try:
		yield "http://projectsedu.com"
	# except GeneratorExit:
	# except BaseException:
	except Exception:
		pass
	yield 2
	yield 3
	return "bobby"


if __name__ == "__main__":
	gen = gen_func()
	print(next(gen))
	# 1. close() 方法会在 执行完的 yield 语句抛出 GeneratorExit 异常,
	# 2. close() 方法会关闭生成器，即便捕获了异常. 也就是说调用方如果继续执行next(gen)会抛异常
	# 3. close() 后, 如果捕获GeneratorExit(不捕没事), 那么生成器不能有后续的 yield 语句，否则抛出 RuntimeError: generator ignored GeneratorExit
	gen.close()
	print("bobby")

# 如果生成器内部"捕获"了异常，那么使用close()后, next(gen)会在 "调用方" 抛出异常

# 如果生成器不去 try...except GeneratorExit, 那么close()不会抛出异常
# 如果生成器  去 try...except Exception,     那么 close() 不会抛出异常

# GeneratorExit 继承自BaseException
# Exception 继承自BaseException


# class GeneratorExit(BaseException):
#     """ Request that a generator exit. """
#     def __init__(self, *args, **kwargs): # real signature unknown
#         pass
#
#     @staticmethod # known case of __new__
#     def __new__(*args, **kwargs): # real signature unknown
#         """ Create and return a new object.  See help(type) for accurate signature. """
#         pass

# class Exception(BaseException):
#     """ Common base class for all non-exit exceptions. """
#     def __init__(self, *args, **kwargs): # real signature unknown
#         pass
#
#     @staticmethod # known case of __new__
#     def __new__(*args, **kwargs): # real signature unknown
#         """ Create and return a new object.  See help(type) for accurate signature. """
#         pass

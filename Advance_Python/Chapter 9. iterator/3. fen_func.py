# 生成器函数，函数只要有关键字yield
def gen_func():
	yield 1
	yield 2
	yield 3
# 惰性求值，延迟求值提供了可能


# 斐波拉契 0 1 1 2 3 5 8 13
def fib(index):
	if index <= 2:
		return 1
	else:
		return fib(index-2) + fib(index-1)
# print(fib(10), "---------fib--------")


def fib2(index):
	lis = []
	a, b = 0, 1
	while index:
		lis.append(b)
		a, b = b, a+b
		index -= 1
	return lis
# print(fib2(10), "---------fib2--------")


def gen_fib(index):
	a, b = 0, 1
	while index:
		yield b
		a, b = b, a+b
		index -= 1
# print(gen_fib(10), "---------gen_fib--------")
# for i in gen_fib(10):
# 	print(i)


def func():
	return 1


if __name__ == "__main__":
	# 生成器对象， python编译字节码的时候就产生了
	gen = gen_func()
	for value in gen:
		print(value)
	# re = func()
	# pass

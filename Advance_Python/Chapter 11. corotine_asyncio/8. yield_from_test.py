# python 3.3 新加了yield from语法

from itertools import chain

my_list = [1, 2, 3]
my_dict = {
	"bobby1": "http://projectsedu.com",
	"bobby2": "http://www.imooc.com",
}

for item in chain(my_list, my_dict):
	print(item)


def my_chain(*args):
	for my_iterable in args:
		yield from my_iterable
		# for value in my_iterable:
		# 	yield value


def g1(iterable):
	yield iterable


def g2(iterable):
	yield from iterable


if __name__ == "__main__":
	for i in my_chain(my_list, my_dict, range(5, 10)):
		print(i)

	for v in g1(range(10)):
		print("g1: ", v)
	for v in g2(range(10)):
		print("g2: ", v)


def g1(gen):
	yield from gen


def main():
	g = g1()
	g.send(None)

# 1. main:调用方  g1:委托生成器  gen:子生成器
# 2. yield from 会在调用方和子生成器之间建立一个双向通道


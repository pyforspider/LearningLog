# 1. python 中函数的工作原理

import inspect
frame = None


def bar():
	global frame
	frame = inspect.currentframe()


def foo():
	bar()


# python.exe 会用一个叫做 PyEvalFrameEx(c函数)去执行foo函数，首先会创建一个栈帧(stack_frame)
"""
python 一切皆对象，栈帧对象， 字节码对象
当foo调用子函数bar， 又会创建一个栈帧
所有的栈帧都是分配在   堆内存   上，这就决定了栈帧可以独立于调用者存在  
(Python 动态语言 函数调用完成，栈帧不会销毁) 
(静态语言函数放在栈内存上，调用完成即销毁)
"""
# import dis
# print(dis.dis(foo))
foo()
print(frame.f_code.co_name)

caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


def gen_func():
	yield 1
	name = 'bobby'
	yield 2
	age = 30
	return 'imooc'

import dis
gen = gen_func()
print(dis.dis(gen))

print(gen.gi_frame.f_lasti)   # -1
print(gen.gi_frame.f_locals)  # {}
next(gen)
print(gen.gi_frame.f_lasti)   # 2    2 YIELD_VALUE
print(gen.gi_frame.f_locals)  # {}
next(gen)
print(gen.gi_frame.f_lasti)   # 12   12 YIELD_VALUE
print(gen.gi_frame.f_locals)  # {'name': 'bobby'}

from collections import UserList
from _collections_abc import Sequence


# 什么是迭代协议
# 迭代器是什么？ 迭代器是访问集合元素的一种方式，一般用来遍历数据
# 迭代器和一下表的访问方式不一样，迭代器是不能反悔的，迭代器提供了一种惰性的方式数据的方法
# [] list , __iter__
# list

from collections.abc import Iterable, Iterator

a = [1, 2]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

iter_rator = iter(a)
print(isinstance(iter_rator, Iterable))
print(isinstance(iter_rator, Iterator))

# class Iterable(metaclass=ABCMeta):
#
#     __slots__ = ()
#
#     @abstractmethod
#     def __iter__(self):    # 只要实现了__iter__ 魔法方法，就是 iterable
#         while False:
#             yield None
#
#     @classmethod
#     def __subclasshook__(cls, C):
#         if cls is Iterable:
#             return _check_methods(C, "__iter__")
#         return NotImplemented
#
#
# class Iterator(Iterable):
#
#     __slots__ = ()
#
#     @abstractmethod
#     def __next__(self):       # iterator 继承自 Iterable, 并且实现 __next__ 魔法方法
#         'Return the next item from the iterator. When exhausted, raise StopIteration'
#         raise StopIteration
#
#     def __iter__(self):
#         return self
#
#     @classmethod
#     def __subclasshook__(cls, C):
#         if cls is Iterator:
#             return _check_methods(C, '__iter__', '__next__')
#         return NotImplemented

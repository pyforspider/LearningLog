# PEP380
# RESULT = yield from EXPR 可以简化成下面这样
# 一些说明
"""
_i：子生成器，同时也是一个迭代器
_y：子生成器生产的值
_r：yield from 表达式最终的值
_s：调用方通过send()发送的值
_e：异常对象


_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r


总结关键点：

1. 子生成器生产的值, 都是直接传给调用方的; 调用方通过.send()发送的值都是直接传递给子生成器的;               line 20
   如果发送的是None, 会调用子生成器的__next__()方法, 如果不是None，会调用子生成器的.send()方法;           line 43
2. 子生成器退出的时候, 最后的return EXPR, 会触发一个StopIteration(EXPR)异常;                           line 15,38,47
3. yield from表达式的值, 是子生成器终止时, 传递给StopIteration异常的第一个参数;                         line 50
4. 如果调用的时候出现StopIteration异常, 委托生成器会恢复运行, 同时其他的异常会向上 "冒泡"；               line 40,49
5. 传入委托生成器的异常里, 除了GeneratorExit之外, 其他的所有异常全部传递给子生成器的.throw()方法;         line 37
   如果调用.throw()的时候出现了StopIteration异常, 那么就恢复委托生成器的运行, 其他的异常全部向上 "冒泡"；  line 40,49
6. 如果在委托生成器上调用.close()或传入GeneratorExit异常, 会调用子生成器的.close()方法, 没有的话就不调用. line 23
   如果在调用.close()的时候抛出了异常, 那么就向上 "冒泡", 否则的话委托生成器会抛出GeneratorExit异常.      line







1. 迭代器（即可指子生成器）产生的值直接返还给调用者
2. 任何使用send()方法发给委派生产器（即外部生产器）的值被直接传递给迭代器。如果send值是None，则调用迭代器next()方法；
   如果不为None，则调用迭代器的send()方法。如果对迭代器的调用产生StopIteration异常，委派生产器恢复继续执行yield from后面的语句；若迭代器产生其他任何异常，则都传递给委派生产器。
3. 子生成器可能只是一个迭代器，并不是一个作为协程的生成器，所以它不支持.throw()和.close()方法,即可能会产生AttributeError 异常。
4. 除了GeneratorExit 异常外的其他抛给委派生产器的异常，将会被传递到迭代器的throw()方法。如果迭代器throw()调用产生了StopIteration异常，委派生产器恢复并继续执行，其他异常则传递给委派生产器。
5. 如果GeneratorExit异常被抛给委派生产器，或者委派生产器的close()方法被调用，如果迭代器有close()的话也将被调用。
   如果close()调用产生异常，异常将传递给委派生产器。否则，委派生产器将抛出GeneratorExit 异常。
6. 当迭代器结束并抛出异常时，yield from表达式的值是其StopIteration 异常中的第一个参数。
7. 一个生成器中的return expr语句将会从生成器退出并抛出 StopIteration(expr)异常。

"""

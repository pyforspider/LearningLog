# 1. 采用同步的方式去编写异步的代码
# 2. 使用单线程去切换任务
# 	1. 线程是有操作系统切换的，单线程切换意味着我们需要程序员自己去调度任务
#   2. 不再需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换， 并发性更高


def get_url(url):
	# do_something 1
	html = get_html(url)  # 此处暂停，切换到另一个函数去执行
	# parse html
	urls = parse_url(html)


def get_url(url):
	# do_something 1
	html = get_html(url)  # 此处暂停，切换到另一个函数去执行
	# parse html
	urls = parse_url(html)


# 传统函数调用 A->B->C
# 我们需要一个可以暂停的函数，并在适当的时候恢复函数的继续执行
# 出现了协程 -> 有多个入口的函数，可以暂停的函数 （可以向暂停的地方传入值）

final_result = {}


def sales_sum(key):
	total = 0
	nums = []
	while True:
		x = yield
		print(key + "销量：", x)
		if not x:
			break
		total += x
		nums.append(x)
	return total, nums


def middle(key):
	# 如果没有while True, 那么在委托生成器返回时，会在调用方 m.send(None) 产生 stop_iteration 异常
	# 在子生成器返回后，while True 结束循环
	# 两种解决方案：1, 委托生成器使用while True   2, 在调用方send(None)捕获异常
	# 关于while True 的解释：  https://blog.csdn.net/luofengmacheng/article/details/89047203
	# while True:
	final_result[key] = yield from sales_sum(key)
	print(key + '销量统计完成')


def main():
	data_sets = {
		'bobby_book': [1200, 1500, 2000],
		'bobby_phone': [28, 55, 98, 108],
		'bobby_cloth': [200, 560, 778, 70],
	}
	for key, data_set in data_sets.items():
		print('start key:', key)
		m = middle(key)
		m.send(None)            # 预激middle协程
		for value in data_set:
			m.send(value)       # 给协程传递的每一组值, 越过中间委托生成器, 直接给子生成器传递值
		try:
			next(m)
		except StopIteration:
			pass
	print('final_result:', final_result)


if __name__ == '__main__':
	main()

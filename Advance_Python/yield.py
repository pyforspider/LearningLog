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
	while True:                  # 没有 while True 在委托结束时，会产生 stop_iteration 异常
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
		m.send(None)
	print('final_result:', final_result)


if __name__ == '__main__':
	main()

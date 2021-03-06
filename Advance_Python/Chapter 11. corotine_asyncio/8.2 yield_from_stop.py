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


if __name__ == "__main__":
	my_gen = sales_sum("bobby牌手机")
	my_gen.send(None)
	my_gen.send(1200)
	my_gen.send(1500)
	my_gen.send(2000)
	try:
		my_gen.send(None)
	except StopIteration as e:    # 在return时会抛异常，且返回结果, 所以必须要捕获异常
		print(e.value)            # 所以 yield from 帮助完成了 异常捕获

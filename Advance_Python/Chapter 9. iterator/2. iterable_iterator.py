from collections.abc import Iterator


class Company(object):
	def __init__(self, employee_list):
		self.employee = employee_list

	def __iter__(self):
		return MyIterator(self.employee)

	# def __getitem__(self, item):
	# 	return self.employee[item]

	def __len__(self):
		return len(self.employee)


# 实现了一个自定义迭代器
class MyIterator(Iterator):
	def __init__(self, employee_list):
		self.index = 0
		self.employee_list = employee_list

	# Iterator 已经实现了__iter__方法，无须重复
	# def __iter__(self):
	# 	return self

	def __next__(self):
		try:
			result = self.employee_list[self.index]
		except IndexError:
			raise StopIteration
		self.index += 1
		return result


if __name__ == "__main__":
	company = Company(['tom', 'bob', 'jane'])

	# 首先寻找对象的__iter__方法，其次寻找__getitem__方法
	# my_itor = iter(company)
	# while True:
	# 	try:
	# 		print(next(my_itor))
	# 	except StopIteration:
	# 		pass

	for item in company:
		print(item)

	print(len(company))

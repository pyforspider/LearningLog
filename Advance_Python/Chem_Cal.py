class IntField:
	def __init__(self):
		self._value = None

	def __get__(self, instance, owner):
		return self._value

	def __set__(self, instance, value):
		if not isinstance(value, int) or value <= 0:
			raise ValueError("你必须输入一个正整数")
		self._value = value


# 属性描述符只能用于类的属性吗？
class Parameter:
	M, m, v = IntField(), IntField(), IntField()


para = Parameter()

# 计算摩尔浓度
stop = True
while stop:
	print("--------------以下计算物质摩尔浓度--------------")

	input_str_M = input('\n请输入该物质的摩尔质量M，即g/mol: ')
	try:
		para.M = int(input_str_M)
	except ValueError:
		# 强行使用属性描述符
		para.M = input_str_M

	input_m = input('请输入所要称取的质量m，单位mg: ')
	para.m = int(input_m)
	n = float(float(para.m)/1000)/int(para.M)
	print("物质摩尔数n：{} mol.".format(n))

	input_v = input('\n请输入溶剂的体积v，单位mL: ')
	para.v = int(input_v)
	c = n/(int(para.v)/1000)
	print("物质摩尔浓度c：{} mol/L.".format(c))

	choice = None
	while True:
		choice = input("\n是否再次计算?(y/n) ")
		if choice not in ["y", "Y", "n", "N"]:
			print("输入无效，请重新输入...")
		else:
			break
	if choice in ["n", "N"]:
		stop = False
	else:
		continue

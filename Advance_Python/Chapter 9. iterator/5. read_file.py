"""
# 500 G, 特殊一行
f = open()
# 方法1
for line in f:
	pass
# 方法2
f.readlines()
# 方法3
# 读取一行
f.read(4096)
"""


def my_read_lines(fb, sep_symbol):
	# 读取缓存，解决一次while循环里 残余数据的遗留，将其合并到下一次读取的 chunk
	buff = ""
	while True:
		while sep_symbol in buff:
			pos = buff.index(sep_symbol)
			yield buff[:pos]
			# 更新缓存为 记号加上分隔符的长度
			buff = buff[pos+len(sep_symbol):]
		# 读取的 组块
		chunk = fb.read(1024)
		# if chunk is None:
		if chunk is "":
			yield buff
			break
		buff += chunk


with open("5.1 input.txt", 'r') as f:
	for line in my_read_lines(f, ","):
		print(line)

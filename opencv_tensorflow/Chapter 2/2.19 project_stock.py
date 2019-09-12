import random

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

date = np.array(range(1, 16))
# date = np.linspace(1, 15, 15)

random_end_price = [random.random()*40+2500+i*10 for i in range(15)]
random_begin_price = [random.random()*40+2500+j*10 for j in range(15)]

end_price = np.array(random_end_price)
begin_price = np.array(random_begin_price)

# 定义一个绘图 ???
# plt.figure()

for i in range(0, 15):
	# 1 柱状图
	dateOne = np.zeros([2])
	# 日期 x
	dateOne[0] = i
	dateOne[1] = i
	# 价格 y
	priceOne = np.zeros([2])
	priceOne[0] = end_price[i]
	priceOne[1] = begin_price[i]
	if end_price[i] > begin_price[i]:
		plt.plot(dateOne, priceOne, "r", lw=8)
	else:
		plt.plot(dateOne, priceOne, "g", lw=8)
plt.show()


# numpy CRUD

import numpy as np

data1 = np.array([[1, 2, 3, 4, 5]])
data2 = np.array([[1, 2, 3],
				  [4, 5, 6]])
print(data1)
print(data2)

# 矩阵维度
print(data1.shape)
print(data2.shape)

# zero & ones
# TensorFlow 和 numpy 批量创建矩阵都要用列表 [x, y] 表示x行y列
print(np.zeros([2, 3]), np.ones([3, 2]))

# CRUD
data2[1, 0] = 5
print(data2)
print(data2[1, 0])

# 与常数的基本运算： 加/减/乘/除法-> 对应相加/减/乘/除
data3 = np.ones([2, 3])
print(data3+2)
print(data3-2)
print(data3*2)
print(data3/2)

# 矩阵间的乘法, numpy矩阵的乘法为 对应的点乘.  这一点与 TensorFlow.multiply(data1, data2) 不同
data4 = np.array([[1, 2, 3],
				  [4, 5, 6]])
print(data3+data4)
print(data3*data4)

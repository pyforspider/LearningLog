# 矩阵加乘法

# 矩阵的大小： M*N
# [[2, 3]]     M=1  N=2
# [[2], [3]]   M=2  N=1
# 矩阵加法： 结果: M*N    M*N = M*N
# 矩阵乘法： 结果：M*N    M*k = k*N


# 矩阵加法： 矩阵的 shape 必须相同
# 矩阵乘法： [A  B]   x   [E  F]   =  [AE+BG  AF+BH]
#           [C  D]       [G  H]      [CE+DG  CF+DH]
# 矩阵乘法要求： 第一个矩阵的列数和第二个矩阵的行数相同

import tensorflow as tf
data1 = tf.constant([[1, 2]])
data2 = tf.constant([[3],
					 [4]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2],
					 [3, 4],
					 [5, 6]])

"""矩阵加乘法运算"""
mat_mul = tf.matmul(data1, data2)
mat_mul2 = tf.multiply(data1, data2)
mat_add = tf.add(data1, data3)
with tf.Session() as sess:
	print(sess.run(mat_mul))         # 矩阵乘法
	print(sess.run(mat_mul2))        # 一般乘法
	print(sess.run(mat_add))

	# 列表封装多个计算
	print(sess.run([mat_mul, mat_add]))


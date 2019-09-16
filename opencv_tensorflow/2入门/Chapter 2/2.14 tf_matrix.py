# 矩阵初识

import tensorflow as tf

"""矩阵"""
# 一行两列矩阵 [[6, 6]]
# 两行一列     [[6], [6]]
data1 = tf.constant([[6, 6]])
data2 = tf.constant([[2],
					 [2]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2],
					 [3, 4],
					 [5, 6]])
# 获取矩阵维度
print(data4.shape)

# 矩阵乘法
data_mut = tf.multiply(data1, data2)
with tf.Session() as sess:
	print(sess.run(data4[0]))        # data4 第一行
	print(sess.run(data4[:, 0]))     # data4 第一列
	print(sess.run(data4[1, 0]))     # data4 第二行 第一列

	print(sess.run(data_mut))




# 批量创建 特殊 矩阵

import tensorflow as tf

# 批量创建矩阵
data1 = tf.constant([[0, 0, 0], [0, 0, 0]])
data2 = tf.zeros([2, 3])
data3 = tf.ones([3, 2])
data4 = tf.fill([233, 466], 699)                 # 233行 466列 的699
with tf.compat.v1.Session() as sess:
	print(sess.run(data1))
	print(sess.run(data2))
	print(sess.run(data3))
	print(sess.run(data4))


# 根据一个矩阵创建一个 相同维度 的矩阵,  相同间隔矩阵,  随机矩阵
data1 = tf.constant([[2], [3], [4]])
data2 = tf.zeros_like(data1)
data3 = tf.linspace(0.0, 2.0, 11)                # [0, 2] 分成10份，共11个数字
data4 = tf.random_uniform([2, 3], -1, 2)         # 2行3列  值区间：[-1, 2]
with tf.compat.v1.Session() as sess:
	print(sess.run(data2))
	print(sess.run(data3))
	print(sess.run(data4))




# tensor 张量 可以是 constant， variable
# operation 可以是 赋值 也可以是 四则运算
# tf本质: graphs(数据操作) = tensor + operation   --->    (session, 运算交互环境)

import tensorflow as tf

"""常量之间的运算"""
data1 = tf.constant(2)
data2 = tf.constant(6)
data_add = tf.add(data1, data2)
data_sub = tf.subtract(data1, data2)
data_mut = tf.multiply(data1, data2)
data_div = tf.divide(data1, data2)

with tf.Session() as sess:
	print(sess.run(data_add))
	print(sess.run(data_sub))
	print(sess.run(data_mut))
	print(sess.run(data_div))

"""常量和变量的运算"""
data1 = tf.constant(2)
data2 = tf.Variable(8)
data_add = tf.add(data1, data2)
data_copy = tf.assign(data2, data_add)     # tf.assign() 委任,将 add 后的结果放入 data2 中. tf中的运算是惰性的，只
data_sub = tf.subtract(data1, data2)       # 有放入 session 中运行才真正运行
data_mut = tf.multiply(data1, data2)
data_div = tf.divide(data1, data2)

init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	print(sess.run(data_add))   # 10

	print(sess.run(data_copy))  # 10
	# 对于计算图的运行，除了sess.run() 方法外，还有以下两种方法:
	# print(data_copy.eval(), "eval")
	# print(tf.get_default_session().run(data_copy), "default")

	print(sess.run(data_sub))   # -8     data2 的数值在此sess中被修改了
	print(sess.run(data_mut))   # 20
	print(sess.run(data_div))   # 0.2

"""定义 placeholder 运算
sess.run(data_calc, feed_dict={data1: value1, data2: value2})
"""
data1 = tf.placeholder(dtype=tf.float32)
data2 = tf.placeholder(tf.float32)
data_mut = tf.add(data1, data2)
with tf.Session() as sess:
	print(sess.run(data_mut, feed_dict={data1: 6, data2: 2}))

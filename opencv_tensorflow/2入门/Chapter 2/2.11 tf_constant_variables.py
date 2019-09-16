# tensorflow 比作 一门开发语言
# 基础的数据类型
# 运算符 流程 字典 数组

import tensorflow as tf

data1 = tf.constant(2.5)
data2 = tf.constant(3, dtype=tf.int32)    # 定点型数据
data3 = tf.Variable(10, name="var")

print(data1)
print(data2)

# with tf.Session() as sess:
with tf.compat.v1.Session() as sess:
	print(sess.run(data1))
	print(sess.run(data2))

# 变量打印前需要先初始化
# init = tf.global_variables_initializer()
init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
	# init 也是一个计算
	sess.run(init)
	print(sess.run(data3))

"""
启动session的两种方法：

sess = tf.compat.v1.Session()
sess.close()

or

with tf.compat.v1.Session() as sess:
"""
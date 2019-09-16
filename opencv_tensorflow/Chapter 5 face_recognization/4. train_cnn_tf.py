# 1 数据yale 2 准备train label-》train
# 3 cnn 4 检测
import tensorflow as tf
import numpy as np
import scipy.io as sio

# Yale 开源文件读取, 15个人，每人11张图片
f = open('Yale_64x64.mat', 'rb')
mdict = sio.loadmat(f)  # keys() --> ['__header__', '__version__', '__globals__', 'gnd', 'fea']
train_data = mdict['fea']   # .shape --> (165, 4096)--> [[1] [1]... [1] [2] [2]...[2]......[15] [15]... [15]] 11x15 165张图, 每一张4096个像素点
train_label = mdict['gnd']  # .shape --> (165, 1)

# 先打乱训练数据, 再选取64张 图和标签 作为测试数据
train_data = np.random.permutation(train_data)
train_label = np.random.permutation(train_label)
test_data = train_data[0:64]  # .shape --> (64, 4096)  64张图, 每一张4096个像素点
test_label = train_label[0:64]
# 再撒100颗种子, 打乱测试数据
np.random.seed(100)
test_data = np.random.permutation(test_data)
np.random.seed(100)
test_label = np.random.permutation(test_label)

# train [0-9 标签] [10个数字*N] [15个人*N]  [0 0 1 0 0 0 0 0 0 0] -> 表示数字2
# 准备训练数据,转换类型，对读入图片进行归一化处理，astype转换数据类型,/255是进行归一化，即像素0-1之间的转化
# 转换完后，train_data数据集为三维，图片数量*64*64，其中64*64为每张图片矩阵的维度，1代表图片是黑白的 (165, 64, 64, 1)
train_data = train_data.reshape(train_data.shape[0], 64, 64, 1).astype(np.float32) / 255  # .shape--> (165, 64, 64, 1)
# 数据集共有15个人，所以建立165*15的数据标签
train_labels_new = np.zeros((165, 15))  # 165张图片 15个人 165张 x [0 0 1 0 0 0 0 0 0 0 0 0 0 0 0] 表示第3个人
for i in range(0, 165):
	j = int(train_label[i, 0]) - 1  # 1-15 转化为 0-14
	train_labels_new[i, j] = 1      # 知道了哪一个下标为1，将训练的数据标签从 0 更新至 1
# 准备测试数据：
test_data_input = test_data.reshape(test_data.shape[0], 64, 64, 1).astype(np.float32) / 255
test_labels_input = np.zeros((64, 15))
for i in range(0, 64):
	j = int(test_label[i, 0]) - 1
	test_labels_input[i, j] = 1

# cnn acc  tf.nn tf.layer
data_input = tf.placeholder(tf.float32, [None, 64, 64, 1])
label_input = tf.placeholder(tf.float32, [None, 15])
#
# layer1 = tf.layers.conv2d(inputs=data_input, filters=32, kernel_size=2, strides=1, padding='SAME',
# 						  activation=tf.nn.relu)
# layer1_pool = tf.layers.max_pooling2d(layer1, pool_size=2, strides=2)
# layer2 = tf.reshape(layer1_pool, [-1, 32 * 32 * 32])
# layer2_relu = tf.layers.dense(layer2, 1024, tf.nn.relu)
# output = tf.layers.dense(layer2_relu, 15)
#
# loss = tf.losses.softmax_cross_entropy(onehot_labels=label_input, logits=output)
# train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
# accuracy = tf.metrics.accuracy(labels=tf.argmax(label_input, axis=1), predictions=tf.argmax(output, axis=1))[1]
#
# # run acc
# init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
# with tf.Session() as sess:
# 	sess.run(init)
# 	for i in range(0, 200):
# 		train_data_input = np.array(train_data)
# 		train_label_input = np.array(train_labels_new)
# 		sess.run([train, loss], feed_dict={data_input: train_data_input, label_input: train_label_input})
# 		acc = sess.run(accuracy, feed_dict={data_input: test_data_input, label_input: test_labels_input})
# 		print('acc:%.2f', acc)

import cv2
import tensorflow as tf

# 定义 TensorFlow 常量
hello = tf.constant("hello, tf")

# 打印常量, 需要使用 session 上下文
sess = tf.compat.v1.Session()
print(sess.run(hello))

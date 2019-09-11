import cv2

# 1.文件的读取 2. 封装格式解析 3. 数据解码 4. 数据加载
img = cv2.imread("test_img.jpg", 1)  # 0-> gray,  1-> color

# jpg png   1 文件头 2 文件数据
cv2.imshow("image", img)

# 程序暂停, 参数为等待时间(ms), 0 永久
cv2.waitKey(2000)

# 图片的写入
# cv2.imwrite(图片的名称.format, 已解码的数据)
cv2.imwrite("copy_img.jpg", img)

img2 = cv2.imread("copy_img.jpg", 0)
cv2.imshow("image2", img2)
cv2.waitKey(2000)

# 读取像素点
# 操作像素点
# 坐标系     [y: 行   x: 列]
import cv2


img = cv2.imread("test_img.jpg", 1)
# 读取（100, 100）
(b, g, r) = img[100, 100]
print(b, g, r)

# 修改像素点
for i in range(100):
	img[10+i, 100] = (255, 255, 0)

cv2.imshow("drew_image", img)
cv2.waitKey(2000)
cv2.imwrite("drew_image.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])


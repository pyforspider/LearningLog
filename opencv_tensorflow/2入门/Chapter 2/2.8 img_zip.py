# jpg, png 图片压缩
# jpg 有损压缩          0-100  图片质量增强, 占用空间变大
# png 无损压缩, 透明度   0-10   图片质量基本不变, 占用空间变小
import cv2

img = cv2.imread("test_img.jpg", 1)

# cv2.imwrite("name.jpg/png", img_data, 列表[写入指定格式的质量, 0-100])
cv2.imwrite("zip_img.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 0])

cv2.imwrite("zip_png.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

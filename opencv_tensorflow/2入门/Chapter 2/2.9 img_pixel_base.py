
"""像素点的一些基本知识"""

# 1. 像素
# 2. 像素的每一个点都由 RGB 三种颜色分量组成
# 3. 颜色深度：8bit 0-255   即8bit(ex: 11001011) 可以表示 256的三次方
#    203 203 9
#    11001011 11001011 00001001
# 4. width high 640*480
# 5. 1.14M = 720*547    *3     *8 bit      /8 (B)    = 1.14 M
#             规格      RGB    二进制大小   单位转换
# 6. RGB alpha 透明度
# 7. RGB   bgr: first_color -> blue
# 8. bgr b: 蓝色分量 g：绿色颜色通道


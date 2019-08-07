import random
from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

from DjangoCache2 import settings


def get_color():
	return random.randrange(256)


def generate_code():
	source = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
	code = ''
	for i in range(4):
		code += random.choice(source)
	return code


def get_rgb_tuple():
	red, green, blue = get_color(), get_color(), get_color()
	rgb_tuple = (red, green, blue)
	return rgb_tuple


# 引用此函数，需要解析ByteIO字节流，如指定 content_type='img/png'
def get_code_pic(code):

	# 设置图片的 模式、(长, 宽)、字体大小、字母个数、混淆点个数
	mode, width, height, font_size, letter_num, point_num = 'RGB', 100, 40, 40, 4, 400

	color = get_rgb_tuple()

	image = Image.new(mode=mode, size=(width, height), color=color)               # 画布
	image_drew = ImageDraw(image, mode=mode)                           # 画笔
	image_font = ImageFont.truetype(settings.FONT_PATH, font_size)     # 设置 字体 大小

	for i in range(4):
		fill = get_rgb_tuple()
		image_drew.text(xy=(width/4*i, 0), text=code[i], font=image_font, fill=fill)	 # 用画笔画字
	for i in range(400):
		fill = get_rgb_tuple()
		image_drew.point(xy=(random.randrange(0, width), random.randrange(0, height)), fill=fill)

	fp = BytesIO()
	image.save(fp, 'png')

	return fp.getvalue()

	# fp = BytesIO()
	# image.save(fp, 'png')
	# return HttpResponse(fp.getvalue(), content_type='img/png')

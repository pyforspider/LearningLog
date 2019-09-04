def g1(gen):
	yield from gen


def main():
	g = g1([1, 2])
	g.send(None)      # 返回 1
	print(next(g))    # 返回 2


if __name__ == "__main__":
	main()

# main 调用方 g1（委托生成器） gen（子生成器）
# yield from 会在 调用方和子生成器 之间建立一个双向通道
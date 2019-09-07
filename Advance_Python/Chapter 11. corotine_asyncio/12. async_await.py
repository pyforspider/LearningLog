# python为了将语义变得更加明确，就引入了 async和await关键词用于定义原生的协程
import types
from collections.abc import Awaitable


async def downloader(url):
	return "bobby"


@types.coroutine
def downloader(url):
	yield "bobby"


async def download_url(url):
	# do sth.
	# await 将控制权交出去，并等待结果返回
	html = await downloader(url)         # await 不能接 async_generator, 而使用 @types.coroutine 只能用生成器yield
	return html


if __name__ == "__main__":
	coro = download_url("http://www.imooc.com")
	# next(coro) XXX  -->  原生协程里面不能用next()来预激协程
	coro.send(None)

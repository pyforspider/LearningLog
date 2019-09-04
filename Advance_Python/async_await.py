import types

# async def downloader(url):
# 	return 'bobby'


@types.coroutine
def downloader(url):
	yield 'bobby'


async def download_url(url):
	html = await downloader(url)
	return html


if __name__ == '__main__':
	coro = download_url('http://www.imooc.com')
	coro.send(None)


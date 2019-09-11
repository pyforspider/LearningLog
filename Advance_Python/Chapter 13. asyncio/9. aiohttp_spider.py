# asyncio 爬虫、去重、入aio_mysql库
# 惨遭 js 反爬
# 并发限制 asyncio.Semaphore(3)

import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery


start_url = 'https://www.csdn.net'
# start_url = 'https://www.jianshu.com'
stopping = False
waitting_urls = []
seen_urls = set()                   # 也可布隆过滤器
sem = asyncio.Semaphore(20)


# 请求一个url, 返回 html 内容
async def fetch(url, session):
	# async with aiohttp.ClientSession() as session:
	# async with sem:
	try:
		async with session.get(url) as resp:
			# print('url status:{}'.format(resp.status))
			# print(resp.status)
			if resp.status in [200, 201]:
				data = await resp.text()
				# print(data)
				return data
	except Exception as e:
		print(e)


# 同步解析 start_url 中可爬取的文章 url 链接. CPU 操作不耗费io, 所以不同 async def ...
def extract_urls(html):
	urls = []
	pq = PyQuery(html)
	for link in pq.items('a'):
		url = link.attr('href')
		if url and url.startswith('http') and url not in seen_urls:
			# print(url)
			urls.append(url)
			waitting_urls.append(url)
	return urls


# 一开始的待爬取url队列为空， 需要从 start_url解析出url
async def init_urls(url, session):
	html = await fetch(url, session)
	seen_urls.add(url)
	extract_urls(html)


# 获取文章详情并解析入库
async def article_handle(url, session, pool):
	html = await fetch(url, session)
	seen_urls.add(url)
	# extract_urls(html)
	try:
		pq = PyQuery(html)
		title = pq('title').text()
		print(title, '-----------title------------')
	except TypeError as e:
		print(e)
	"""
	problem
	"""
	# async with pool.acquire() as conn:
	# 	async with conn.cursor() as cur:
	# 		await cur.execute("SELECT 42;")
	# 		insert_sql = "insert into article_test(title) values('{}')".format(title)
	# 		await cur.execute(insert_sql)


# 1. 调度协程函数 asyncio.ensure_future(coroutine)
# 2. 不停地从 waiting_urls 中获取数据, 当列表中有数据时, 就启动协程去完成, 将协程扔进asyncio, 将asyncio看做协程池
async def consumer(pool):
	async with aiohttp.ClientSession() as session:
		while not stopping:
			if len(waitting_urls) == 0:
				await asyncio.sleep(0.5)
				continue
			url = waitting_urls.pop()
			print('start to get url: {}'.format(url))
			if re.match('https://blog.csdn.net/.*?', url):
			# if re.match('http://www.jianshu.com/.*?', url):
				if url not in seen_urls:
					# 提交一个 [文章解析] 的协程
					print(url, "------------matched_url----------")
					asyncio.ensure_future(article_handle(url, session, pool))
					# await asyncio.sleep(0.1)
			# else:
			# 	if url not in seen_urls:
			# 		# 子url不是文章的url，那么 [解析子url中的url]
			# 		asyncio.ensure_future(init_urls(url, session))


# 爬虫 主逻辑
async def main(loop):
	# 等待mysql连接建立好
	pool = await aiomysql.create_pool(
									host='127.0.0.1', port=3306,
									user='root', password='shaojian',
									db='aiomysql_test', loop=loop, charset="utf8", autocommit=True)

	# 当下面的ensure_future()提交后，不等待返回，session被close，后续的 init_urls()就不能调用session
	# async with aiohttp.ClientSession() as session:
	# 	asyncio.ensure_future(init_urls(start_url, session))
	# asyncio.ensure_future(consumer(pool))

	async with aiohttp.ClientSession() as session:
		# await 需要等待返回才执行后续代码，而 asyncio.ensure_future() 仅提交了一个协程
		await init_urls(start_url, session)
		# html = await fetch(start_url, session)
		# seen_urls.add(start_url)
		# extract_urls(html)
	asyncio.ensure_future(consumer(pool))
	# await consumer(pool)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	asyncio.ensure_future(main(loop))
	loop.run_forever()
	# print(len(seen_urls))

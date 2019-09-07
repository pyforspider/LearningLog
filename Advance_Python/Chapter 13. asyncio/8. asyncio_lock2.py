import asyncio
from asyncio import Lock, Queue

import aiohttp

cache = {}
lock = Lock()


async def get_stuff(url):
	async with lock:
		if url in cache:
			return cache[url]
		stuff = await aiohttp.request('GET', url)
		cache[url] = stuff
		return stuff


async def parse_stuff():
	stuff = await get_stuff()
	# do some parsing


async def use_stuff():
	stuff = await get_stuff()
	# use stuff to sth. interesting


tasks = [parse_stuff(), use_stuff()]

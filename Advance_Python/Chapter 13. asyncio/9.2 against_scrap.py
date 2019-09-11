# import asyncio
#
#
# async def hello():
#     await asyncio.sleep(1)
#     print('Hello')
#     return 'World'
#
# loop = asyncio.get_event_loop()
# r = loop.run_until_complete(hello())
# print(r)
# loop.close()
#
# string = "abc 111"
# if string.startswith("abc"):
#     print('a')

import requests


def getHTMLtext(url):
    try:
        response = requests.get(url)
        print(response.url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except Exception as e:
        print(e)


r = getHTMLtext("https://blog.csdn.net/csdnnews/article/details/100550182")
print(r)

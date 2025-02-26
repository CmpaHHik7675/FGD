import asyncio
import aiohttp

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response. text()

async def main():
    await asyncio.gather(q(), w(), e(), r(), t(), y(), u(), i(), o(), p() )

async def q():
    html1 = await fetch("https://jsonplaceholder.typicode.com/posts/1")
    print(html1)

async def w():
    html2 = await fetch("https://jsonplaceholder.typicode.com/posts/2")
    print(html2)

async def e():
    html3 = await fetch("https://jsonplaceholder.typicode.com/posts/3")
    print(html3)
    
async def r():
    html4 = await fetch("https://jsonplaceholder.typicode.com/posts/4")
    print(html4)
    
async def t():
    html5 = await fetch("https://jsonplaceholder.typicode.com/posts/5")
    print(html5)
    
async def y():
    html6 = await fetch("https://jsonplaceholder.typicode.com/posts/6")
    print(html6)
    
async def u():
    html7 = await fetch("https://jsonplaceholder.typicode.com/posts/7")
    print(html7)
    
async def i():
    html8 = await fetch("https://jsonplaceholder.typicode.com/posts/8")
    print(html8)
    
async def o():
    html9 = await fetch("https://jsonplaceholder.typicode.com/posts/9")
    print(html9)
    
async def p():
    html10 = await fetch("https://jsonplaceholder.typicode.com/posts/10")
    print(html10)
    
asyncio.run(main())


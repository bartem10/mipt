из коллекций импорт namedtuple
 время импорта
импорт asyncio
от параллельных. фьючерсные импортные FIRST_COMPLETED
из aiohttp импорт ClientSession
 сокет импорта


Сервис = именованныйтуплее('Сервис', ('имя', 'url', 'ip_attr'))

УСЛУГИ = (
    Сервис('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Сервис('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(сервис, сеанс): # получение ip
    асинхронизация с сеансом. получить(услуга. url) в качестве ответа:
        data = ждать ответа. json()
        вернуть данные[сервис. ip_attr]



async def asynchronous():# создание футур для сервисов
                         # используйте FIRST_COMPLETED
    async с ClientSession() в качестве сеанса:
        задачи = [asyncio. create_task(fetch_ip(сервис, сессия)) для обслуживания в СЕРВИСАХ]
        done, pending = await asyncio. wait(задачи, timeout=Нет, return_when=FIRST_COMPLETED)
        для будущего в готовом:
            печать(будущее. результат())


asyncio. run(асинхронный())
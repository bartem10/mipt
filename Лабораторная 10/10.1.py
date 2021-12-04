импорт asyncio

асинхронный деффакториал(имя, число):
    f = 1
    для i в диапазоне(2, число + 1):
        print(f"Task  {name}: Compute factorial({i})...")
        ждать асинхронио. сон(1)
        f *= i
    print(f"Task  {name}: factorial({number}) =  {f}")

async def main():
    ждать асинхронио. собирать(
        факториал("А", 2),
        факториал("B", 3),
        факториал("С", 4),
    )

loop = asyncio. get_event_loop()
петля. run_until_complete(главная())
петля. закрывать()
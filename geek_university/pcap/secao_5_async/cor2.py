import asyncio


async def diz_oi_demorado():
    print('Oi...')
    await asyncio.sleep(2)
    # Vamos usar o await sempre quando formos executar uma função asyncrona
    # E também não usamos o await em função que não seja asyncrona ou seja -> async def faz_algo():
    print('todos...')


el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demorado())
el.close()

# await diz_oi_demorado()

import asyncio

# A palavra reservado async transforma a nossa função em uma corrotina
async def diz_oi():
    print('oi...')


# el = Event Loop
el = asyncio.get_event_loop()
el.run_until_complete(diz_oi())
el.close()

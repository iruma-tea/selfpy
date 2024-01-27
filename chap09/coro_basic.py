import asyncio


# 疑似的な「重い」処理
async def heavy_process(name, sec):
    print(f'start {name}')
    # ダミーの重い処理(sec秒だけ処理を休止)
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'

print(heavy_process('Hoge', 5))

def gen_com():
    while True:
        n = yield input('名前を教えてください:')
        # sendメソッドからの値でメッセージを生成
        yield f'こんにちは、{n}さん！'


gen = gen_com()
for name in gen:
    # ジェネレーターからの戻り値を再送信
    res = gen.send(name.upper())
    print(res)

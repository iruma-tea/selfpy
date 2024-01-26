# デコレーターの引数を受け取る
def log_func(details=True):
    # 修飾すべき関数を受け取る
    def outer(func):
        # 本来の関数に渡すべき引数を受け取る
        def inner(*args, **keywds):
            print('----------------------')
            print(f'Name: {func.__name__}')
            if details:
                print(f'Args: {args}')
                print(f'Keywds: {keywds}')
            print('----------------------')
            return func(*args, **keywds)
        return inner
    return outer


@log_func(details=False)
def hoge(x, y, m='bar', n='piyo'):
    print(f'hoge: {x}-{y}/{m}-{n}')


hoge(15, 37, m='ほげ', n='ぴよ')

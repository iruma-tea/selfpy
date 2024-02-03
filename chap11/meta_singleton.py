class SingleTonMeta(type):
    # 実クラスにクラス変数を追加
    def __init__(cls, name, bases, disc, **kwargs):
        cls.__instance = None

    # 実クラスをインスタンス化する際の処理を追加
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class MySingleTon(metaclass=SingleTonMeta):
    pass


if __name__ == '__main__':
    c1 = MySingleTon()
    c2 = MySingleTon()
    print(c1 is c2)

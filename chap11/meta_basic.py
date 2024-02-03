class MyMeta(type):
    @classmethod
    def __prepare__(metacls, __name: str, __bases: tuple[type, ...], **kwds):
        print(f'{metacls}: __prepare__')
        return {'hoge': 'ほげ'}

    def __new__(metacls, __name, __bases, __disc, **kwargs):
        print(f'{metacls}: __new__')
        return super().__new__(metacls, __name, __bases, __disc)

    def __init__(cls, __name, __bases, __disc, **kwargs):
        print(f'{cls}: __init__')
        return super().__init__(__name, __bases, __disc)

    def __call__(cls, *args, **kwargs):
        print(f'{cls}: __call__')
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    pass


if __name__ == '__main__':
    c = MyClass()
    print(MyClass.hoge)

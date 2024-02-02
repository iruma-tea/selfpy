class Person:
    __slots__ = ['__firstname', '__lastname']

    def __init__(self, firstname, lastname) -> None:
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    def __delattr__(self, __name: str) -> None:
        raise RuntimeError

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.firstname == other.firstname and \
                self.lastname == other.lastname
        return False

    def __hash__(self) -> int:
        return hash((self.firstname, self.lastname))


if __name__ == '__main__':
    p = Person('太郎', '山田')
    dic = {p: '男'}
    print(dic[p])

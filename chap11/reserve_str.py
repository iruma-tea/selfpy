class Person:
    def __init__(self, firstname, lastname) -> None:
        self.__firstname = firstname
        self.__lastname = lastname

    def __str__(self) -> str:
        return f'{self.lastname} {self.firstname}'

    def __repr__(self) -> str:
        return f'{Person({self.firstname}, {self.lastname})}'

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname


if __name__ == '__main__':
    p = Person('太郎', '山田')
    print(p)

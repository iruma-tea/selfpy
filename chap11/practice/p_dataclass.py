import dataclasses


@dataclasses.dataclass()
class Hamster:
    name: str
    age: int = 0

    def show(self):
        print(f'{self.name}は{self.age}歳です！')


if __name__ == '__main__':
    h = Hamster('のどか', 1)
    h.show()

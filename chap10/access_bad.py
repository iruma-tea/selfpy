class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f'私の名前は{self.name}、{self.age}歳です！')

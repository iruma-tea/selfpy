class Area:
    # 円周率
    PI = 3.14

    @classmethod
    def circle(cls, radius):
        return radius * radius * cls.PI


if __name__ == '__main__':
    print(Area.PI)
    print(Area.circle(10))

class Left:
    def __init__(self, value) -> None:
        self.value = value

    def __sub__(self, other):
        print('Left#__sub__')
        return Left(self.value - other.value)


class Right:
    def __init__(self, value) -> None:
        self.value = value

    def __rsub__(self, other):
        print('Right#__rsub__')
        return Right(other.value - self.value)


if __name__ == '__main__':
    l = Left(10)
    r = Right(5)
    result = l - r
    print(result.value)

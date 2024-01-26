data = 'global'


def outer():
    data = 'outer'

    def inner():
        nonlocal data
        data = 'inner'
        return data
    print(inner())
    print(data)


outer()
print(data)

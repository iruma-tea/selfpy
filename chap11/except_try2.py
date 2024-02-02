def hoge():
    try:
        return 'Hoge'
    finally:
        print('**Finally**')


if __name__ == '__main__':
    print('Start')
    print(hoge())
    print('End')

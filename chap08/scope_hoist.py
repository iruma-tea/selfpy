num = 3


def check_scope():
    print(num)  # エラー
    num = 108
    return num


print(check_scope())

# 高級関数walk_list関数
def walk_list(data, func):
    # リストの内容を順に処理
    for key, value in enumerate(data):
        # func経由で指定の関数を呼び出し
        func(value, key)

# リストを処理するためのユーザー定義関数


def show_item(value, key):
    print(key, ':', value)


data = [105, 53, 27, 87, 33]
walk_list(data, show_item)

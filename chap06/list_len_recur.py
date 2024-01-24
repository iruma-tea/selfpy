# 入れ子のリストの要素数をカウント
def recursive_len(data):
    result = 0
    if isinstance(data, list):
        # 要素がlistであれば、配下の内容を順にカウント
        for elem in data:
            result += recursive_len(elem)
    else:
        # 要素がlistでなければ、要素数は1
        result = 1
    return result


d_list = [
    [15, 87,
     [1, 3, 5, 7]
     ],
    58,
    [2, 4, 6, 8, 10],
]

print(recursive_len(d_list))

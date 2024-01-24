import copy

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# data2 = data.copy() # 変更が互いに影響を与える
data2 = copy.deepcopy(data)
data2[0][0] = 1000
print(data)
print(data2)

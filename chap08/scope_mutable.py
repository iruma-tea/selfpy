def param_update(data):
    data[0] = 55
    return data


data = [2, 4, 6]
print(param_update(data)[0])
print(data[0])

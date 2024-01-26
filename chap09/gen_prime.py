import math


# 素数を求めるジェネレータ
def get_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# 引数valueが素数であるかどうか判定
def is_prime(value):
    result = True
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result


# 素数を順に出力
for prime in get_prime():
    print(prime)
    if prime > 100:
        break

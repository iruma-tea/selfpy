# arg1は位置引数であること
def my_func(arg1, /, arg2=0, arg3=0):
    pass


# my_func(arg1=10, arg2=20)
my_func(10, arg2=20)

def my_gen():
    yield 'あいうえお'
    yield 'かきくけこ'
    yield 'さしすせそ'


for value in my_gen():
    print(value)

try:
    raise Exception('例外発生')
except Exception as ex:
    print(ex.args[0])
finally:
    print('**Finally**')

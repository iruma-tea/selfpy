d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
# print(d['pear'])  # エラー KeyError
print(d.get('pear', '×'))
print(d.pop('melon', '×'))
print(d.popitem())
print(d)

rank = '甲'

msg = {
    '甲': '大変良いです。',
    '乙': '良いです。',
    '丙': 'がんばりましょう。'
}

if rank in msg:
    print(msg[rank])
else:
    print('???')

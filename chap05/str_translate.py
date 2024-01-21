msg = '今日は,あなたの運勢は,●よい感じ●です.'

print(msg.translate(str.maketrans({
    ',': '、',
    '.': '。',
    '●': ''
})))

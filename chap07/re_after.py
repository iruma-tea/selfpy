import re

msg = '<p>サポートサイト<a href="https://wings.msn.to/">https://wings.msn.to/</a></p>'

ptn = re.compile(r'<a href="(.+?)">\1</a>')
results = ptn.finditer(msg)
for result in results:
    print(result.group())

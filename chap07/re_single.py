import re

msg = 'はじめまして。\nよろしくお願いします。'

ptn = re.compile(r'^.+', re.DOTALL)
results = ptn.findall(msg)
for result in results:
    print(result)

import re
import json

pattern = re.compile(r'[0-9]*\.')
data = []
x = -1

for line in open('batman.txt').read().split('\n'):
    if re.match(pattern, line):
        x += 1
        data.append('')
    else:
        data[x] += line + '\n'
    
with open('batman.json', 'w') as out:
    json.dump(data, out)

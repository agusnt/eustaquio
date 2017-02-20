#!/usr/bin/python3

import re
import json

data = []
first = False
author = ""

for line in open('communism.txt').read().split('\n'):
    if line == "":
        first = True
        continue
    if first is True:
        author = line
        first = False
    else:
        data.append(line + " - " + author)
    
with open('communism.json', 'w') as out:
    json.dump(data, out)

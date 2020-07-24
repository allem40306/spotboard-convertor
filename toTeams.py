import sys
import json
import re

content = []
teams = []


for s in sys.stdin:
    s = re.sub('\s', ',', s)
    s = s.replace('\n', '')
    r = s.split(",")
    teams.append({"id":int(r[1]),"name":r[2]+" (FJCU) "})
content.append({"teams": teams})

file = open('teams.json', 'w')
json.dump(list(teams), file)
import sys
import json

content = []
runs = []


for s in sys.stdin:
    r = s.split(",")
    run = []
    if(str(r[4].replace('\n','')) == "Yes"):
        run={"id":int(r[0]),"team":int(r[1]),"problem":int(ord(r[2][0])-ord('A'[0])),"result":"Yes","submissionTime":int(r[3])}
    else:
        run={"id":int(r[0]),"team":int(r[1]),"problem":int(ord(r[2][0])-ord('A'[0])),"result":"No - Wrong Answer","submissionTime":int(r[3])}
    runs.append(run)
content.append({"runs": runs})

file = open('test.json', 'w')
json.dump(list(runs), file)
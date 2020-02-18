import json

data = {"name":"liudana","age":23}

with open(r't.json','w') as f:
    json.dump(data,f)


with open(r't.json','r') as f:
     d = json.load(f)
     print(d)
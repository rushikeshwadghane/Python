ip = ["eat", "tea", "tan", "ate", "nat", "bat"]

op =  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

res = {}
for i in ip:
    key =  "".join(sorted(i))
    if res.get(key,None):
        res[key].append(i)
    else:
        res[key] = [i]

print(list(res.values()))




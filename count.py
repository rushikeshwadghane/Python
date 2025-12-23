arr = [1,2,4,1,2,3,4,5,6,7,5,4,5,6,]

dup = {}
dup_items = []
for i in arr:
    cnt = dup.get(i,0)
    dup.update({i:cnt+1})
    if cnt == 2:
        dup_items.append(i)

new_dict = {}

print(dup)


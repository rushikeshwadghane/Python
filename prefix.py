arr = ["flower", "flow", "flight"]
arr = ["dog", "racecar", "car"]

l = len(arr[0])
pref = ""
for i in range(l):
    flag = False
    word = arr[0][i]
    for j in range(1,len(arr)):
        if len(arr[j]) > i:
            compare = arr[j][i]
            if(word == compare):
                flag = True
            else:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        pref += arr[0][i]
print(pref)

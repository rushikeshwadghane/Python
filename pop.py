phrase = "Don't Panic"
plist = list(phrase)

print(phrase)
print(plist)
size =  len(plist)
print(size)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
print(plist)
plist.insert(2,plist.pop(3))
print(plist)
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)    
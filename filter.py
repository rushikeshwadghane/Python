from ast import Lambda


list1 = [12,34,56,76,44,22,45,66,77,43]

Evenlist = filter(lambda x:x%2==0,list1)

print(Evenlist)
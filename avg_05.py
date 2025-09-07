t = int(input())
l = []
for i in range(t):
    m,n = input().split()
    try:
        k = int(m)/int(n)
        l.append(k)
    except ZeroDivisionError as e:
        l.append(e)
    except Exception as e:
        l.append(e)

for j in l:
    print('Error Code: ',j)

        
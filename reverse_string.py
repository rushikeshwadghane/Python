
# def reverse_string(s):
#     str = list(s)

#     l = 0
#     r =len(s) - 1

#     while l < r:
#         str[l] ,str[r] = str[r], str[l]
#         l += 1
#         r -= 1
#     return "".join(str)
        
# def reverse_string1(s):
#     s[:3]  = s[2::-1]
#     return s


# # res =  reverse_string("hello")
# # res1 =  reverse_string1("hello")
# res1 =  reverse_string1([1,2,3,4,5])
# #32145
# # print(res)
# print(res1)
    
# a = [1,2,[3,4]]
# b = a
# b[2][0] = 100

# print(a)
# print(b)
# print(id(b))

# min = float('-inf')
# print(min)




# def reverse1(sent:str):
#     sent =  sent.split('.')
#     print(sent)
#     sent.reverse()
#     print(sent)
#     sent =  ".".join(sent)
#     # s = s.removeprefix("##").removesuffix("!!")

#     print(sent)



# print([1,3,4]== [3,1,4])


# def checkEqual(a, b) -> bool:
#     ac = {}

#     for i in a:
#         c =  ac.get(i,0)
#         ac[i] = c + 1
    
#     for j in b:
#         c = ac.get(j,None)
#         if c != None:
#             ac[j] = c - 1
#     f =  True
#     print(ac)
#     for k,v in enumerate(ac):
#         print(k,v)
#         if ac= 0:
            
#             f= False
#             # break
            
#     return f

# a = [1 ,2 ,5 ,4 ,0]
# b = [2 ,4 ,5 ,0 ,1]
# r = checkEqual(a,b)

# print(r)


# def pushZerosToEnd(arr):
#     pos = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[i],arr[pos] = arr[pos] ,arr[i]
#             pos += 1
            
#     print(arr)


# pushZerosToEnd([3, 5, 0, 0, 4])



def nthFibonacci(n: int) -> int:
    
    c = 1
    a = 0
    b = 1
    while c < n:
        t = a + b
        print(t,'--------',a,'------------',b)
        a = b
        b = t
        c += 1
    print('fibo',t)

nthFibonacci(5)
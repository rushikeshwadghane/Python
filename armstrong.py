
num = input("enter num")
l = len(list(num))
print(l)

class Solution:
    def armstrong(self, num):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** l
            temp //= 10
        if num == sum:
            return True
        else:
            return False
        

res = Solution()
result = res.armstrong(int(num))
if result:
    print(num, "is armstrong")  
else:
    print(num, "is not armstrong")
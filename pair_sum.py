

class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i] + arr[j] == arr[k]:
                        return True
        
        return False


object = Solution()
a = [6865, 8921, 22468, 20392, 27390, 31530, 8847, 26964, 20505, 21692, 7535, 31540, 18233, 19549, 30152, 12717, 28032, 25526, 23414, 7868, 26691, 22744, 18960, 28208, 6250, 7192, 30569, 10775, 7450, 22557]
res = object.findTriplet(a)
print(res)
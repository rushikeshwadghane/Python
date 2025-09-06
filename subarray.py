#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        
        l = len(arr)
        left = 0
        current_sum = 0
        for i in range(l):
            current_sum  += arr[i]
            print(current_sum, left, i)
            while current_sum > target and  left <= i:
                print(current_sum, left, i,'<<<<<<<<<<<<')
                current_sum -= arr[left]
                left+= 1
                
            if current_sum == target:
                return [left+1 ,i +1 ]
                
        return -1


obj = Solution()

# res = obj.subarraySum([1,2,3,7,5], 12)
res = obj.subarraySum( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)

print(res)
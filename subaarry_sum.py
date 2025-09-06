class Solution:
    def maxSubarraySum(self, arr):
        max_sum = arr[0]
        current_sum  = arr[0]
        l  = len(arr)
        for i in range(1,l):
            cs = current_sum + arr[i]
            ci = arr[i]
            print('cs','ci',cs,ci)
            if ci > cs:
                current_sum = ci
            else:
                current_sum = cs
            
            if current_sum > max_sum:
                max_sum = current_sum
            

            # current_sum = max(cs,ci)
            # max_sum = max(max_sum,current_sum)


        return max_sum
    
obj  = Solution()

res = obj.maxSubarraySum([-1,0,8,4])

print('ressssssss',res)
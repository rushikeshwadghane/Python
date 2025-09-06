class Solution:
    def minJumps(self, arr):
        n = len(arr)

        # if array has one element, we are already at the end
        if n <= 1:
            return 0

        # if first element is 0, we cannot move anywhere
        if arr[0] == 0:
            return -1

        # initialization
        maxReach = arr[0]   # max index we can currently reach
        steps = arr[0]      # steps we can still take
        jumps = 1           # we have to take at least one jump

        for i in range(1, n):
            # we reached the end
            if i == n - 1:
                return jumps

            # update maxReach
            maxReach = max(maxReach, i + arr[i])

            # use a step
            steps -= 1

            # if no steps left
            if steps == 0:
                jumps += 1

                # check if current index is beyond maxReach
                if i >= maxReach:
                    return -1

                # reinitialize steps with the number of steps
                # we can take from the new range
                steps = maxReach - i

        return -1
        

# Test
obj = Solution()
res = obj.minJumps([1, 3, 5 ,8, 9, 2, 6, 7, 6, 8, 9])
print('Minimum jumps =', res)

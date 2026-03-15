class Solution:
    def distinctAdjacentElement(self, arr):
        n = len(arr)

        # manual frequency map
        freq = {}
        maxFreq = 0

        for x in arr:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

            # manually track maximum
            if freq[x] > maxFreq:
                maxFreq = freq[x]

        # ceil(n/2) without using math
        limit = (n + 1) // 2

        if maxFreq <= limit:
            return True
        return False


object = Solution()

res = object.distinctAdjacentElement([3, 3,3, 9, 7, 7, 5, 6, 2, 2])
print(res)
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) <2:
            return -1
        f = s = -1
        for n in arr:
            if n > f:
                s = f
                f = n
            
            elif f > n > s:
                s = n

                
        return s
                
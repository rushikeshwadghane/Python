
class Solution:
    def merge_and_sort(self, list1, list2):
        merged_list = set(list1 + list2)
        new = sorted(list(merged_list))
        return new  # remove duplicates and return sorted list
    

object = Solution()
list1 = [27, 77, 12, 7, 18]
list2 = [11,32]
result = object.merge_and_sort(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
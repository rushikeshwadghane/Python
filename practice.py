# def valueEqualToIndex(arr):
#     if len(arr) == 1 and arr[0] == 1:
#         return [1]

#     res   = []    
#     for i in range(len(arr)):
#         print(arr[i],'------',i)
#         if arr[i] == i+1:
#             res.append(arr[i])
            
#     return res
 
# # arr = [15 ,2, 45 ,12 ,7]
# arr  = [1,1]
# print(valueEqualToIndex(arr))


# def gcd(self,a,b):
#     if b == 0:
#         return a
#     return self.gcd(b,a%b)
        
        
# def lcmAndGcd(self, a : int, b : int) -> List[int]:
#     g =  self.gcd(a,b)
#     l = (a*b) // g
#     return [l,g]
        

# def f(arr):
#     res = []
#     for i in arr:
#         if isinstance(i,list):
#             res.extend(f(i))
#         else:
#             res.append(i)
#     return res

# arr =  [1,[13,14],2,3,4,[5,6,7,[8,9,[12,[1212,1212]]],10],11,12]
# print(f(arr))


# def firstOccindex(txt,pat):
#         n = len(txt)
#         m = len(pat)
#         i = 0
#         j = 0
#         fo = -1
#         while i < n:
#             if j >= m:
#                 break
#             print(i,j)
#             if txt[i] == pat[j]:
#                 if fo == -1:
#                     fo = i
#                 j += 1
#             else:
#                 if fo >= 0:
#                     i =  fo
#                     fo = -1 
#                     j = 0
#             i += 1
#         return fo
                 
            
        # j = 0 
        # f = -1
        # for i in range(len(txt)):
            
        #     if j < len(pat):
        #         print(f,txt[i],pat[j],i,j)
        #         if txt[i] == pat[j]:
        #             if f == -1:
        #                 f = i
        #             j += 1

        #         else:
        #             if f > 0:
        #                 f = -1
        #                 j = 0
        #             if txt[i] == pat[j]:
        #                 if f == -1:
        #                     f = i
        #                 j += 1
        # return f  

# print(firstOccindex('nxtipemjbxualljkxgbbwmkxouqeyegvkildhxcqsfayer','bwmkxouqeyegvkildhxcqsfayer'))
# print(firstOccindex('kkyxinsuusfbyfvikw','kw'))
# print(firstOccindex('aaaaaaaaa','aaa'))
# print(firstOccindex('GeeksForGeeks','Fr'))

# def check_pal(arr):
#     for i in arr:
#         i = str(i)
#         if i != i[::-1]:
#             return False
#     return True
    
# arr = [111, 222, 333, 444, 555]
# print(check_pal(arr))


class Node:
    def __init__(self,data,next = None):
        self.value  = data
        self.next = None

class BuildLinkedList:
    def build_ll(self,arr):
        if not arr:
            return None

        head = Node(arr[0])
        temp = head
        for i in range(1,len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return head
    
    def print_ll(self,head):
        tt = head
        r = []
        while tt:
            r.append(tt.value)
            tt = tt.next
        print(r)
    def merge_two_link_list(self,head1,head2):

        temp = Node(-1)
        curr = temp

        while head1 and head2:
            if head1.value <= head2.value:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next
        curr.next  = head1 if head1 else head2
    
        tt = temp.next
        r  = []
        while tt:
            r.append(tt.value)
            tt = tt.next
        print(r)

        
    def deleteDuplicates(self, head):
        temp = head
        while temp and temp.next:
            if temp.value == temp.next.value:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
l1 = [1,1,2,3,3]
# l2 = [1,3,4,5]

obj = BuildLinkedList()
head = obj.build_ll(l1)

# head2 = obj.build_ll(l2)
# obj.merge_two_link_list(head1,head2)
res = obj.deleteDuplicates(head)
obj.print_ll(res)




# def romanToInt(s: str) -> int:
#     roman = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }

#     total = 0
#     prev_value = 0
#     # s = s[::-1]
#     for char in  s[::-1]:
#         value = roman[char]
#         if value < prev_value:
#             total -= value
#         else:
#             total += value

#         prev_value = value
#     return total

# s = "MCMXCIV"
# # print(s[::-1])
# Output: 1994

# print(romanToInt(s))

# a = [1,3,4,2,4,9,5,7,8]
# s = 'dfgfgghrtg'

# # print(a.sort())
# print(a)
# print(sorted(a))
# print(sorted(s))



1,1,1,2


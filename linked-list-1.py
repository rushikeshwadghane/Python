class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head  = new_node
            return 
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            # print(temp)

l = Linkedlist()
for i in range(5):
    l.append(i)

l.print_list()





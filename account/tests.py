# from django.test import TestCase

# class Node:
#     def __init__(self,data=None,next=None) -> None:
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def inspect(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
        
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

    
#     def append(self,data):
#         node = Node(data,self.head)
#         self.head = node

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.append(data)

# n = Node()
# l = LinkedList()
# l.append([5,10,15,20])
# l.append('cow')
# l.append('goat')
# l.inspect()

def merge(my_list):
    if len(my_list) > 1:
        left_split = my_list[:len(my_list)//2]
        right_split = my_list[len(my_list)//2:]

        merge(left_split)
        merge(right_split)

        i = 0
        j = 0
        k = 0

        while i < len(left_split)  and j < len(right_split):
            if left_split[i] < right_split[j]:
                my_list[k] = left_split[i]
                i +=1
               
            else:
                my_list[k] = right_split[j]
                j+=1
               
            k += 1
        print('left',left_split)
        print('right',right_split)
        
        while i < len(left_split):
            my_list[k] = left_split[i]
            i+=1
            k += 1

        while j < len(right_split):
            my_list[k] = right_split[j]
            j+=1
            k += 1
  
un_s = [5,2,7,3,10,7,8,9]
merge(un_s)
#print(un_s)

















# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            list1 = list2
        else:
            temp = list1
            while temp.next != None:
                temp = temp.next
            temp.next = list2
        
        temp = list1
        arr = []

        while temp != None:
            arr.append(temp.val)
            temp=temp.next
        arr = sorted(arr)
        print(arr)
        if len(arr) == 0:
            return None
        output = ListNode(val=arr[0])
        temp = output
        for i in range(1, len(arr)):
            new  = ListNode(val=arr[i])
            temp.next = new 
            temp = temp.next
        return output

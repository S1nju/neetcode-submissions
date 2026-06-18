# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

            

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp  != None:
            arr.append(temp.val)
            temp = temp.next
        arr = list(reversed(arr))
        if arr == []:
            return head
            
        head = ListNode(val = arr[0])
        temp = head
        for i in range(1,len(arr)):
            new = ListNode(val = arr[i])
            temp.next = new
            temp = temp.next
        return head
            


        



        
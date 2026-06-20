# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return 
        temp = head
        listlen = 0
        while temp != None  :
            listlen+=1
            temp = temp.next

        temp= head
        temp2 = head
        i=0
        if listlen-n ==0 :
            return head.next

        while temp != None :
            if i ==  listlen-n:
             temp2.next = temp.next
             return head
            temp2 = temp
            i=i+1
            temp = temp.next
        return head

        
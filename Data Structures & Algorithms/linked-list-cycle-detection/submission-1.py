# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        temp = head
        seen = []
        while temp not in seen:
            seen.append(temp)
            if temp.next !=None:
                temp= temp.next
            
        if seen[-1].next != None:
            return True
        return False
        
        
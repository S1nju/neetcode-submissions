# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_lists = []
        if len(lists)==0:
            return None
        print(lists)
        for el in lists:
            if  el:
                temp = el
                while temp :
                    merged_lists.append(temp.val)
                    temp = temp.next
    
        print(merged_lists)
        merged_lists = sorted(merged_lists)
        newh = ListNode(val = merged_lists[0])
        temp = newh 
        for i in range(1,len(merged_lists)):
            new =  ListNode(val = merged_lists[i])
            temp.next = new 
            temp = temp.next
        return newh
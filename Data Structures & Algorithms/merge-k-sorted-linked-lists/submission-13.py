# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                res.append(self.mergeTwoList(list1, list2))
            lists = res
        
        return lists[0]

    def mergeTwoList(self, l1, l2):
        dummy = ListNode()
        res = dummy

        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next
            
        if l1:
            res.next = l1
        if l2:
            res.next = l2

        return dummy.next
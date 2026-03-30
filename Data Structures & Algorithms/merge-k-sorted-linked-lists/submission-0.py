# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge two sorted linked lists, divide and conquer
        if not lists or len(lists) == 0:
            return None

        # keep cutting the lists in half
        while len(lists) > 1:
            res = []
            
            # iterate through each of the lists, increment by 2 because of each pair of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # list2 could be null
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # merge the lists and put it into res
                res.append(self.mergeList(l1, l2))
            # update our lists variable
            lists = res
        # return the last list available
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    
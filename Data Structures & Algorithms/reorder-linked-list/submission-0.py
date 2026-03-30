# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer
        # two lists, reverse the second list

        # slow and fast pointers to find the split of the two lists
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # start of second list will the slow.next
        secondList = slow.next

        # want to reverse the second list
        slow.next = None
        prev = None
        while secondList:
            tmp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = tmp
        
        # merge the two halfs
        firstList, secondList = head, prev
        while secondList:
            tmp1, tmp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = tmp1
            firstList, secondList = tmp1, tmp2








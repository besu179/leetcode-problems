# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
# this algorithm works by creating 2 pointers named fst and slow pointers 
# the concept is fast pointer goes twice as fast as the slow one therefor
# if fast pointer is at the end of the linked list slow must be in the middle
# 
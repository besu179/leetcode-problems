# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast, mid = head, head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next

        cur, prev = mid, None
        while cur:
            nxt = cur.next  
            cur.next = prev 
            prev = cur     
            cur = nxt     

        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            prev = prev.next
            head = head.next

        return ans

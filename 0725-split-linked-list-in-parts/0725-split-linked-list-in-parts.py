# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        if not head:
            return [None] * k

        n = 0
        cur = head

        while cur:
            cur = cur.next
            n += 1
        
        size = n // k
        remainder = n % k

        ans = []
        cur = head

        for i in range(k):
            ans.append(cur)

            cur_size = size + (1 if i < remainder else 0)

            for j in range(cur_size - 1):
                if cur:
                    cur = cur.next
                
            if cur:
                next_head = cur.next
                cur.next = None
                cur = next_head
        return ans
            
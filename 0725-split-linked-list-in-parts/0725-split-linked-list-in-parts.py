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
            n += 1
            cur = cur.next

        part_size = n // k
        extra = n % k

        ans = []
        cur = head

        for i in range(k):
            head_part = cur
            size = part_size + (1 if i < extra else 0)

            for j in range(size - 1):
                if cur:
                    cur = cur.next

            if cur:
                next_part = cur.next
                cur.next = None
                cur = next_part

            ans.append(head_part)

        return ans
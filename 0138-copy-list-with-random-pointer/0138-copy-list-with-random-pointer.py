# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        if not head:
            return None

        hm = {}

        cur = head
        while cur:
            hm[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                hm[cur].next = hm[cur.next]
            if cur.random:
                hm[cur].random = hm[cur.random]
            cur = cur.next

        return hm[head]
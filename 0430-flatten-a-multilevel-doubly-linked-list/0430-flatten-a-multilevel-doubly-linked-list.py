"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head

        cur = head
        stack = []

        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.child.prev = cur
                cur.next = cur.child
                cur.child = None

            elif not cur.next and stack:
                nxt = stack.pop()
                cur.next = nxt
                nxt.prev = cur

            cur = cur.next

        return head
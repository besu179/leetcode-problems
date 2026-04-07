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

        cur = head

        while cur:
            node = Node(cur.val)   
            node.next = cur.next
            cur.next = node
            cur = node.next
        
        temp = head
        while temp:
            node = temp.next
            if temp.random:
                node.random = temp.random.next
            temp = node.next

        new_head = head.next
        temp = head
        while temp:
            node = temp.next

            temp.next = node.next
            if node.next:
                node.next = node.next.next

            temp = temp.next

        return new_head
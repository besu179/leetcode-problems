class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        count = 0
        cur = self.head
        while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        dummy = Node(val)

        dummy.next = self.head
        self.head = dummy
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.head
        dummy = Node(val)

        if not self.head:
            self.head = dummy
            return

        while cur.next:
            cur = cur.next
        cur.next = dummy

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        dummy = Node(val)
        cur = self.head

        if index == 0:
            self.addAtHead(val)
            return

        for _ in range(index-1):
            
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        dummy.next = cur.next
        cur.next = dummy


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur = self.head

        if not self.head:
            return 

        if index == 0:
            self.head = self.head.next
            return

        for _ in range(index - 1):
            if not cur or not cur.next:
                return
            cur = cur.next
        if not cur.next:
            return
        cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
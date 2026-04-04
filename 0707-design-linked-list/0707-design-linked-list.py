class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        dummy = Node(val)
        dummy.next = self.head
        self.head = dummy

        if self.size == 0:
            self.tail = dummy
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        dummy = Node(val)
        if self.size == 0:
            self.head = self.tail = dummy
        else:
            self.tail.next = dummy
            self.tail = dummy
        self.size += 1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        dummy = Node(val)
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        dummy.next = cur.next
        cur.next = dummy

        self.size += 1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return

        cur = self.head
        for _ in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next

        if index == self.size - 1:
            self.tail = cur

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
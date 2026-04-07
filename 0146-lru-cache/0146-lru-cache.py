class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)

        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.rmv(self.cache[key])
            self.insrt(self.cache[key])
            return self.cache[key].val
        return -1


    def rmv(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insrt(self, node):
        prv, nxt = self.latest.prev, self.latest
        prv.next = node
        node.prev = prv
        node.next = nxt
        nxt.prev = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.rmv(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insrt(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.rmv(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
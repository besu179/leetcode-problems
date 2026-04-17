class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.n = 0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == self.value:
            self.n += 1
        else:
            self.n = 0
        return self.n >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.acc = [0]
        for x in nums:
            self.acc.append(self.acc[-1] + x)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.acc[right + 1] - self.acc[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
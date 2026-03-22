class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        ls = 0

        for i in range(len(nums)):
            if ls == total - ls - nums[i]:
                return i
            ls += nums[i]
        return -1
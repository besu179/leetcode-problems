class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        the given solution will optimize space to O(1)
        '''
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
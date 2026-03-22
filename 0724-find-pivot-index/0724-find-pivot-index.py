class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s_left = [nums[0]]
        s_right = [0] * (n + 1)

        for i in range(len(nums)- 1, -1, -1):
            s_right[i] += s_right[i + 1] + nums[i]

        for i in range(1, len(nums)):
            s_left.append(nums[i] + s_left[i - 1])

        for i in range(n):
            if s_left[i] == s_right[i]:
                return i
                
        return -1
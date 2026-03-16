class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = s = 0
        ans = float('inf')

        for r in range(len(nums)):
            s += nums[r]
            while s >= target and l < len(nums):
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0
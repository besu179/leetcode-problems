class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        l = cur_sum = 0
        cur_window = set()

        for r in range(len(nums)):
            while nums[r] in cur_window:
                cur_sum -= nums[l]
                cur_window.remove(nums[l])
                l += 1
            cur_window.add(nums[r])
            cur_sum += nums[r]
            ans = max(ans, cur_sum)
        return ans
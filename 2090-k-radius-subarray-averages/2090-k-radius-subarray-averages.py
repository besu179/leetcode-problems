class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * n
        l = cur_sum = 0
        valid_length = 2*k+1

        for r in range(n):
            cur_sum += nums[r]
            if r - l + 1 == valid_length:
                ans[l + k] = cur_sum // valid_length
                cur_sum -= nums[l]
                l += 1
        return ans
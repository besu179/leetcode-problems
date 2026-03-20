class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = ans = s = 0
        hm = defaultdict(int)

        for r in range(len(nums)):
            s += nums[r]
            hm[nums[r]] += 1

            if r - l + 1 > k:
                s -= nums[l]
                hm[nums[l]] -= 1
                if hm[nums[l]] == 0:
                    del hm[nums[l]]
                l += 1
            if len(hm) == k:
                ans = max(ans, s)
        return ans
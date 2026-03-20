class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = ans = oddcount = gap = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                oddcount +=1
            if oddcount == k:
                gap = 0

                while oddcount == k:
                    oddcount -= nums[l] % 2
                    l += 1
                    gap += 1
            ans += gap
        return ans
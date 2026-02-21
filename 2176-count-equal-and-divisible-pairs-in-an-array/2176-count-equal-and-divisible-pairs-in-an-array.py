class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans +=1
        return ans
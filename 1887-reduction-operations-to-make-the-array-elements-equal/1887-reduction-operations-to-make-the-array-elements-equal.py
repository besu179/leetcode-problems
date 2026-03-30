class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        steps = ans = 0
        cur = nums[0]

        for i in range(len(nums)):
            if cur != nums[i]:
                steps += 1
                cur = nums[i]
            ans += steps
        return ans
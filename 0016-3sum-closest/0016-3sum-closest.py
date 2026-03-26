class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[right] + nums[left]
                if abs(three_sum - target) < abs(ans - target):
                    ans = three_sum
                if three_sum > target:
                    right -= 1
                else:
                    left += 1
                
        return ans
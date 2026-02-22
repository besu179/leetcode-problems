class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        front = 0
        back = len(nums) - 1
        ans = [-1, -1]
        
        while front < len(nums):
            if ans[0] == -1 and nums[front] == target:
                ans[0] = front
            if ans[1] == -1 and nums[back] == target:
                ans[1] = back
            if ans[0] != -1 and ans[1] != -1:
                break
            front += 1
            back -= 1
        return ans
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        front = 0
        back = len(nums) - 1

        while front <= back:
            if nums[front] == val:
                nums[front], nums[back] = nums[back], nums[front]
                back -= 1
            else:
                front += 1
        return front

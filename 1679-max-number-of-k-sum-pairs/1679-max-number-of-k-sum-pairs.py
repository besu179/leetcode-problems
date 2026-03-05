class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans, front, last = 0, 0, len(nums) - 1

        while front < last:
            cur_sum = nums[front] + nums[last]
            if cur_sum == k:
                front += 1
                last -= 1
                ans += 1
            elif  cur_sum > k:
                last -= 1
            else:
                front += 1

        return ans
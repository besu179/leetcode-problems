class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If we've seen the number needed to reach the target, return
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, add current number to the dictionary
            seen[num] = i
            
        return []
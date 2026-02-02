class Solution(object):
    def majorityElement(self, nums):
        key_val = {}
        for val in nums:
            key_val[val] = key_val.get(val, 0) + 1
        
        mid = len(nums) // 2
        
        for ky, count in key_val.items():
            if count > mid:
                return ky

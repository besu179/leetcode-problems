class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        key_val = {}
        ans = []
        min_appearance = len(nums) // 3
        for val in nums:
            key_val[val] = key_val.get(val, 0) + 1
        
        for ky, val in key_val.items():
            if val > min_appearance:
                ans.append(ky)
        return ans
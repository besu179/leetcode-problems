class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = list(set(nums))
        
        arr.sort(reverse=True)
        
        if len(arr) < 3:
            return arr[0]
        return arr[2] 
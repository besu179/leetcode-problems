class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hm = {0: -1}
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k
            
            if remainder in hm:
                if i - hm[remainder] > 1:
                    return True
            else:
                hm[remainder] = i
                
        return False
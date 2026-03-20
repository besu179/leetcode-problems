class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = Counter()
        n = len(nums)
        l = 0
        pairs = 0
        ans = 0
        
        for r, num in enumerate(nums):
            pairs += counter[num]
            counter[num] += 1
            
            while pairs >= k:
                ans += n - r
                counter[nums[l]] -= 1
                pairs -= counter[nums[l]]
                l += 1
                
        return ans
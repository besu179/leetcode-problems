class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        
        total_sum = sum(cardPoints)
        
        if k == n:
            return total_sum
            
        window_size = n - k
        
        current_window_sum = sum(cardPoints[0:window_size])
        min_window_sum = current_window_sum
        
        l = 0
        for r in range(window_size, n):
            current_window_sum += cardPoints[r] - cardPoints[l]
            
            min_window_sum = min(min_window_sum, current_window_sum)
            
            l += 1
            
        return total_sum - min_window_sum
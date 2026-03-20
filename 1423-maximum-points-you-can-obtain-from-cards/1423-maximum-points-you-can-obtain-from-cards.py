class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """        
        s = sum(cardPoints)
                    
        cur_sum = sum(cardPoints[0:len(cardPoints) - k])
        min_sum = cur_sum
        
        l = 0
        for r in range( len(cardPoints) - k, len(cardPoints)):
            cur_sum += cardPoints[r] - cardPoints[l]
            min_sum = min(min_sum, cur_sum)
            l += 1
            
        return s - min_sum
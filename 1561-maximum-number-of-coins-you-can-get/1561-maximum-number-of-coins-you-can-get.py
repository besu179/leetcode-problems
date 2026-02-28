class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        ans = 0
        arr = piles[len(piles) // 3 : : 2]
        for val in arr:
            ans += val
        return ans
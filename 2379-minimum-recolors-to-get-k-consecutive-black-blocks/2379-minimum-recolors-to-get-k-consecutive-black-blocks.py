class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        hm = Counter(blocks[:k])
        ans = hm['W']
        l = 0

        for r in range(k, len(blocks)):
            hm[blocks[r]] += 1
            hm[blocks[l]] -= 1
        
            l += 1
            ans = min(ans, hm["W"])
        return ans
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        l, ans = 0, n
        hm = Counter(s)
        
        for r in range(n):                               
            hm[s[r]] -= 1                              

            while l < n and 4*max(hm.values()) <= n:    
                ans = min(ans, r-l+1)                
                hm[s[l]] += 1 
                l += 1

        return ans
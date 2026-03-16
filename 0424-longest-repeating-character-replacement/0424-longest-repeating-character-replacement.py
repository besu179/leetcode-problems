class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hm = {}
        l = ans = 0

        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            while (r - l + 1) - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans
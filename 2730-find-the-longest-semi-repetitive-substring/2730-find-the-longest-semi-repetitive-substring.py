class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = ans = pairs = 0

        for r in range(len(s)):
            if r > 0 and s[r] == s[r - 1]:
                pairs += 1
            while pairs > 1:
                if s[l] == s[l + 1]:
                    pairs -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = defaultdict(int)
        ans = l = 0

        for r in range(len(s)):
            hm[s[r]] += 1

            while l < len(s) and len(hm) != (r - l + 1):
                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1
            if (r - l + 1) > ans:
                ans = r - l + 1

        return ans
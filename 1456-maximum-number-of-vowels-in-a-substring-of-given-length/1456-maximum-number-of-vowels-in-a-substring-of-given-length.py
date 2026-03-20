class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
        v_count = l = 0

        for i in range(k):
            if s[i] in vowels:
                v_count += 1
        ans = v_count
        for r in range(k, len(s)):
            if s[l] in vowels:
                v_count -= 1
            l += 1
            if s[r] in vowels:
                v_count += 1
            ans = max(ans, v_count)
        return ans
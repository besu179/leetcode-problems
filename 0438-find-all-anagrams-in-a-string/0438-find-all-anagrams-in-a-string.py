class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        phm = counter(p)

        l = 0
        ans = []

        for r in range(len(s)):"""
        result = []
        target_counts = Counter(p)
        window_counts = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            curr_char = s[i]
            window_counts[curr_char] += 1
            if window_counts == target_counts:
                result.append(i - len(p) + 1)
            window_counts[s[i - len(p) + 1]] -= 1
            if window_counts[s[i - len(p) + 1]] == 0:
                del window_counts[s[i - len(p) + 1]]
        return result
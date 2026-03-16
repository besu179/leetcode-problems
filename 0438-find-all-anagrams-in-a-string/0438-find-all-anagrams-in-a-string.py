class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        phm = Counter(p)
        thm = Counter(s[:len(p) - 1])
        ans = []

        for r in range(len(p) - 1, len(s)):
            thm[s[r]] += 1
            if thm == phm:
                ans.append(r - len(p) + 1)
            thm[s[r - len(p) + 1]] -= 1
            if thm[s[r - len(p) + 1]] == 0:
                del thm[s[r - len(p) + 1]]

        return ans
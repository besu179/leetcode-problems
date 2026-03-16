class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        phm = Counter(p)
        thm = Counter(s[:len(p)])
        ans = []

        if thm == phm:
            ans.append(0)

        for r in range(len(p), len(s)):
            thm[s[r]] += 1
            
            left_char = s[r - len(p)]
            thm[left_char] -= 1
            if thm[left_char] == 0:
                del thm[left_char]

            if thm == phm:
                ans.append(r - len(p) + 1)

        return ans
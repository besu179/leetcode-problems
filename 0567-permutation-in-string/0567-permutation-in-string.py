class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hm1 = Counter(s1)
        hm2 = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            hm2[s2[r]] = 1 + hm2.get(s2[r], 0)
            
            while (r - l + 1) > len(s1):
                hm2[s2[l]] -= 1
                
                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]
                l += 1
            if hm2 == hm1:
                return True
            
        return False
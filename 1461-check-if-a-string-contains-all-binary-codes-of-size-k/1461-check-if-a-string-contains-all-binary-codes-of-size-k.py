class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        visited = set()

        for i in range(len(s) - k + 1):
            visited.add(s[i : i+k]) # see 

            if len(visited) == 2 ** k :
                return True
        return False
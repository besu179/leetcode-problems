class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        iterat = iter(s)

        for i, j in enumerate(t):
            if j not in iterat:
                return len(t) - i
        return 0
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        
        s = list(str(abs(num)))
        
        if num > 0:
            s.sort()
            # Find the first non-zero digit to swap to the front
            for i, digit in enumerate(s):
                if digit != '0':
                    s[0], s[i] = s[i], s[0]
                    break
            return int("".join(s))
        else:
            # For negative, sort descending to get the "largest" magnitude
            s.sort(reverse=True)
            return -int("".join(s))
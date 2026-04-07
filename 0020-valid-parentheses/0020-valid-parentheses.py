class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        pairs = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in pairs:
                stk.append(char)
            else:
                if not stk or pairs[stk.pop()] != char:
                    return False
        
        return not stk
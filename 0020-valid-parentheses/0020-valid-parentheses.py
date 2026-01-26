class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = [] # create a python list to act as a stack
        pairs = { "(":")", "{":"}", "[":"]" } # pairs of values that close each other

        for char in s:
            if char in pairs.keys():
                stk.append(char)
            elif char in pairs.values():
                if not stk:
                    return False
                if pairs.get(stk[-1]) == char:
                    stk.pop(len(stk) - 1)
                else:
                    return False
        return len(stk) == 0 # returns the length of stack being 0 or not (empty is true)
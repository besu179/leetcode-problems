class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
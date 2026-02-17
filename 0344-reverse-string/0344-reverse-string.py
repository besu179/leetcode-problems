class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        front = 0
        back = len(s) - 1
        while front < back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
        return s
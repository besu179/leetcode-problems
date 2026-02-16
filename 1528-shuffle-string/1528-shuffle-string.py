class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        word = [None] * len(s)
        
        for i, char in enumerate(s):
            word[indices[i]] = char
            
        return "".join(word)

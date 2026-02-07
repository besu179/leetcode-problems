class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        for word in words:
            wrd = set(word.lower())
            if wrd <= row1 or wrd <= row2 or wrd <= row3:
                ans.append(word)
        return ans
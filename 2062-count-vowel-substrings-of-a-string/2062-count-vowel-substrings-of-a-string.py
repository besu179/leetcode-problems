class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = "aeiou"
        ans = 0
        
        for i in range(len(word)):
            cur = set()
            for j in range(i, len(word)):
                if word[j] in vowels:
                    cur.add(word[j])
                    if len(cur) == 5:
                        ans += 1
                else:
                    break
        return ans
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        dic = {}
        for char in words[0]:
            dic[char] = dic.get(char, 0) + 1

        for word in words[1:]:
            for char in dic.keys():
                current_count = word.count(char)
                
                if current_count < dic[char]:
                    dic[char] = current_count
        
        for key, value in dic.items():
            ans += [key] * value
        
        return ans

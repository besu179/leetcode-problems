class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for char in magazine:
            if dic.get(char):
                dic[char] +=1
            else:
                dic[char] = 1
            
        for char in ransomNote:
            if char not in dic.keys() or ransomNote.count(char) > dic[char]:
                return False
        return True

# dictionary is like a hashmap 
# to access elements in the dictionary  dic[key] and dic.get(key) can be used 
# get(key) is the efficint one to use if it not found it will return None
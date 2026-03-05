class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = Counter(s).most_common()

        ans = [key * val for key, val in d]
        return "".join(ans)
#.most_common() returns a list of tuples: [('e', 2), ('r', 1), ('t', 1)] from most frequent to less
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = Counter(s)
        d = d.most_common()

        ans = [key * val for key, val in d]
        return "".join(ans)
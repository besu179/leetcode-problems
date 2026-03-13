class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ss = sorted(score, reverse=True)
        ans = []
        dic = {}

        for i in range(len(ss)):
            if i == 0:
                dic[ss[i]] = "Gold Medal"
            elif i == 1:
                dic[ss[i]] = "Silver Medal"
            elif i == 2:
                dic[ss[i]] = "Bronze Medal"
            else:
                dic[ss[i]] = str(i + 1)
        for s in score:
            ans.append(dic[s])

        return ans
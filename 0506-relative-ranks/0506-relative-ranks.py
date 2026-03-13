class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_score = sorted(score, reverse=True)
        ans = []
        dic = {}

        for i in range(len(sorted_score)):
            if i == 0:
                dic[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                dic[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                dic[sorted_score[i]] = "Bronze Medal"
            else:
                dic[sorted_score[i]] = str(i + 1)
        for sc in score:
            ans.append(dic[sc])
        return ans
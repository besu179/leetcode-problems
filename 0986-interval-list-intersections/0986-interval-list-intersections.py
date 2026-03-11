class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        ans = []

        while i < len(firstList) and j < len(secondList):
            a_s, a_e = firstList[i]
            b_s, b_e = secondList[j]

            if a_s <= b_e and b_s <= a_e:
                ans.append([max(a_s, b_s), min(a_e, b_e)])
            if a_e <= b_e:
                i += 1
            else:
                j += 1
        return ans
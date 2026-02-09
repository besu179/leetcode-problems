class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i

        min_sum = float('inf')
        ans = []

        for j in range(len(list2)):
            word = list2[j]
            if word in dict1:
                index_sum = dict1[word] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    ans = [word]
                elif index_sum == min_sum:
                    ans.append(word)

        return ans
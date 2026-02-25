class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(names)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]
        return names
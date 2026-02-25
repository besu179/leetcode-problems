class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(names)
        for i in range(1, n):
            j = i - 1
            key_height = heights[i]
            key_name = names[i]

            while j >= 0 and heights[j] < key_height:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = key_height
            names[j + 1] = key_name
        return names
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        arr = []
        for num in nums:
            if dic[num] == 2:
                arr.append(num)

        return list(set(arr))
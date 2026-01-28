class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        leng = len(nums3)
        medium = leng//2
        if leng % 2 == 0:
            return (nums3[medium] + nums3[medium - 1]) / 2.0
        return nums3[medium]
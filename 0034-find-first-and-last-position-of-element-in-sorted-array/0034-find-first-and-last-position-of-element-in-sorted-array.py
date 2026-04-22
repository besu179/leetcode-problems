class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst():
            idx = -1
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    idx = mid
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return idx

        def findLast():
            idx = -1
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    idx = mid
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return idx

        return [findFirst(), findLast()]
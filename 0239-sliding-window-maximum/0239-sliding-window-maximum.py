class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        ans = []

        for right in range(len(nums)):
            while q and q[0] < right - k + 1:
                q.popleft()

            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if right >= k - 1:
                ans.append(nums[q[0]])

        return ans
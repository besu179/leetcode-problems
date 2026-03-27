class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)

        for booking in bookings:
            ans[booking[0] - 1] += booking[2]
            ans[booking[1]] -= booking[2]
        tmp = 0

        for i in range(n):
            tmp += ans[i]
            ans[i] = tmp
            
        return ans[:n]
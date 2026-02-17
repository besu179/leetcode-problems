class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        n = len(seats) - 1
        ans = 0

        while n >= 0:
            ans += abs(students[n] - seats[n])
            n -= 1
            
        return ans
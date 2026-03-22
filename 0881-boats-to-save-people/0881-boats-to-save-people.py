class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        ans = 0

        l, r = 0, len(people) - 1

        while l <= r:
            if people[r] == limit:
                ans += 1
            elif people[r] + people[l] <= limit:
                ans += 1
                l += 1
            else:
                ans += 1
            r -= 1
        return ans
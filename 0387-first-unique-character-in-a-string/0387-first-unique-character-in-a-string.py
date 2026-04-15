class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = {}
        q = deque()

        for i, char in enumerate(s):
            c[char] = c.get(char, 0) + 1
            q.append((char, i))

            while q and c[q[0][0]] > 1:
                q.popleft()

        return q[0][1] if q else -1
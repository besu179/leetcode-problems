class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for cur_idx, cur_temp in enumerate(temperatures):
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = cur_idx - prev_idx
            
            stack.append(cur_idx)
            
        return ans
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            
            diff[start] += val
            diff[end + 1] -= val
        
        current_shift = 0
        res = list(s)
        
        for i in range(n):
            current_shift += diff[i]
            
            original_pos = ord(res[i]) - ord('a')
            
            new_pos = (original_pos + current_shift) % 26
            
            res[i] = chr(new_pos + ord('a'))
            
        return "".join(res)
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
    
        diff = [0] * (n + 1)
        
        for l, r, direction in shifts:
            val = 1 if direction == 1 else -1
            
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val
        
        for i in range(1, n):
            diff[i] += diff[i - 1]
        
        ans = []
        
        for i in range(n):
            shift = diff[i] % 26
            
            char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            ans.append(char)
        
        return "".join(ans)
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # 1. Sort first to make first and last the most different
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        ans = ""
        
        # 2. Compare characters only between the most different strings
        for c in range(min(len(first), len(last))):
            if first[c] != last[c]:
                return ans
            ans += first[c]
            
        return ans

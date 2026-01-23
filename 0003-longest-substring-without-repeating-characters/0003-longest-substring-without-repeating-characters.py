class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # If character is found in the current window, move left pointer
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            # Update the last seen index of the character
            char_map[s[right]] = right
            
            # Calculate and update the maximum length
            max_length = max(max_length, right - left + 1)
            
        return max_length

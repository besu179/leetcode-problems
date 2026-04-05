class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needed_counts = Counter(t)
        needed_unique = len(needed_counts)

        relevant_chars = [
            (i, ch) for i, ch in enumerate(s) if ch in needed_counts
        ]

        left = 0  
        formed_unique = 0 
        window_counts = {}  


        best = (float("inf"), None, None)

        for right, (right_index, right_char) in enumerate(relevant_chars):
            window_counts[right_char] = window_counts.get(right_char, 0) + 1

            if window_counts[right_char] == needed_counts[right_char]:
                formed_unique += 1

            while formed_unique == needed_unique:
                left_index, left_char = relevant_chars[left]

                window_length = right_index - left_index + 1
                if window_length < best[0]:
                    best = (window_length, left_index, right_index)

                window_counts[left_char] -= 1
                if window_counts[left_char] < needed_counts[left_char]:
                    formed_unique -= 1

                left += 1

        return "" if best[0] == float("inf") else s[best[1] : best[2] + 1]
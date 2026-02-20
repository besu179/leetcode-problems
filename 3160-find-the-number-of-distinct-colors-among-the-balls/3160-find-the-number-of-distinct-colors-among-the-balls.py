class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_to_color = {}
        color_count = Counter()
        result = []
      
        for ball_number, new_color in queries:
            color_count[new_color] += 1
          
            if ball_number in ball_to_color:
                old_color = ball_to_color[ball_number]
                color_count[old_color] -= 1
              
                if color_count[old_color] == 0:
                    color_count.pop(old_color)
          
            ball_to_color[ball_number] = new_color
          
            result.append(len(color_count))
      
        return result
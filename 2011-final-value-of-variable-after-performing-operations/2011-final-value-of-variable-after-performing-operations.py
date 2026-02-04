from collections import Counter

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        counts = Counter(operations)

        return counts['++X'] + counts['X++'] - counts['--X'] - counts['X--']
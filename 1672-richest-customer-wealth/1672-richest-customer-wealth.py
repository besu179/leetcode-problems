class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest = sum(accounts[0])
        # Python function sum returns the sum of elements in the list works for number
        # Meanwhile it is not specified in the qusestion we may have -ve maximun.
        for m in range(1, len(accounts)):
            wealth = sum(accounts[m])
            if wealth > highest:
                highest = wealth
        return highest
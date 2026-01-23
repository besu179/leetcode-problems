class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1, n + 1):
            if i % 3 == i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
                # i got a problem implementing the double quotes i tried to use f"{i}" but
                # it does not go as i assumed. 
                # str() method converts numbers to string s in python .
        return arr

# Here is a solution from google
# Time and space complexity O(n)
'''
class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n + 1):
            # 1. Create an empty string for each number
            msg = ""
            
            # 2. Check conditions and concatenate
            if i % 3 == 0:
                msg += "Fizz"
            if i % 5 == 0:
                msg += "Buzz"
                
            # 3. If msg is still empty, the number wasn't divisible by 3 or 5
            if not msg:
                msg = str(i)
                
            ans.append(msg)
        return ans
    '''
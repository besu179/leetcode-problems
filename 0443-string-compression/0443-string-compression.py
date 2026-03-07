class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = write = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                count += 1
                read +=1
            
            chars[write] = char
            write += 1
            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1

        return write
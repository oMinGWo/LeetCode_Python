class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        if len(chars) <= 1:
            return len(chars)

        count = 0
        char = chars[0]
        result = []
        for c in chars:
            if c == char:
                count += 1
            else:
                result.append(char)
                if count > 1:
                    for co in str(count):
                        result.append(co)
                count = 1
                char = c
        result.append(char)
        if count > 1:
            for co in str(count):
                result.append(co)
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)
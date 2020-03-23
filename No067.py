class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        j = len(b) - 1
        c = 0
        result = ''
        while i >= 0 or j >= 0:
            x = a[i] if i >= 0 else 0
            y = b[j] if j >= 0 else 0
            t = int(x) + int(y) + c
            if t == 2:
                t = 0
                c = 1
            elif t == 3:
                t = 1
                c = 1
            else:
                c = 0
            result = str(t) + result
            i -= 1
            j -= 1
        if c == 1:
            result = '1' + result
        return result


if __name__ == '__main__':
    s = Solution()
    print s.addBinary('1010', '1011')

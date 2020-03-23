class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        jin = 0
        index = 0
        l1 = len(num1)
        l2 = len(num2)
        result = ''
        while index < max(l1, l2):
            a = num1[l1 - 1 - index] if l1 - 1 - index >= 0 else 0
            b = num2[l2 - 1 - index] if l2 - 1 - index >= 0 else 0
            t = int(a) + int(b) + jin
            if t < 10:
                jin = 0
            else:
                jin = 1
                t = t % 10
            result = str(t) + result
            index += 1

        if jin == 1:
            result = '1' + result
        return result


if __name__ == '__main__':
    s = Solution()
    print s.addStrings('123', '456')

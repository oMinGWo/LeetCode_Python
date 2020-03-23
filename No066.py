class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = 1
        result = []
        for i in range(len(digits) - 1, -1, -1):
            m = digits[i] + n
            if m >= 10:
                n = 1
                result.insert(0, 0)
            else:
                n = 0
                result.insert(0, m)

        if n == 1:
            result.insert(0, n)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.plusOne([4, 3, 2, 1])

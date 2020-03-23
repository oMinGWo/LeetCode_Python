class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        for i in range(len(s)):
            c = s[i]
            if c == 'M':
                result += 1000
            elif c == 'D':
                result += 500
            elif c == 'C':
                if i == len(s) - 1:
                    result += 100
                elif s[i + 1] == 'D' or s[i + 1] == 'M':
                    result -= 100
                else:
                    result += 100
            elif c == 'L':
                result += 50
            elif c == 'X':
                if i == len(s) - 1:
                    result += 10
                elif s[i + 1] == 'L' or s[i + 1] == 'C':
                    result -= 10
                else:
                    result += 10
            elif c == 'V':
                result += 5
            else:
                if i == len(s) - 1:
                    result += 1
                elif s[i + 1] == 'V' or s[i + 1] == 'X':
                    result -= 1
                else:
                    result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('III')
    print s.romanToInt('MCMXCIV')

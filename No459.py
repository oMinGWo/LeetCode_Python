class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(len(s) / 2, 0, -1):
            if len(s) % i != 0:
                continue
            base = s[0:i]
            ok = True
            for j in range(1, len(s) / i):
                com = s[i * j:i * j + i]
                if base != com:
                    ok = False
                    break
            if ok:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.repeatedSubstringPattern('aaa')

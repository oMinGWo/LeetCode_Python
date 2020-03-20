class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        map = {}
        for c in s:
            if c in map:
                map[c] = map[c] + 1
            else:
                map[c] = 1

        m = 0
        result = 0
        for key in map.keys():
            if map[key] % 2 == 1:
                m = 1
                result += map[key] - 1
            else:
                result += map[key]

        return result + m


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome('abccccdd')
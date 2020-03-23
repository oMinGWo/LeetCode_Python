class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        ss = s.split(" ")
        result = 0
        for word in ss:
            if word.lstrip() != '':
                result += 1

        return result


if __name__ == '__main__':
    s = Solution()
    print s.countSegments('a b c   d,e   xxx')

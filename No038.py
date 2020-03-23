class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # result = [
        #     '1',
        #     '11',
        #     '21',
        #     '1211',
        #     '111221'
        # ]
        # if n <= 5:
        #     return result[n - 1]

        index = 1
        s = '1'
        while index < n:
            count = 0
            c = s[0]
            i = 0
            ss = ''
            while i < len(s):
                if s[i] == c:
                    count += 1
                else:
                    ss = ss + str(count) + str(c)
                    c = s[i]
                    count = 1
                i += 1
            if i == len(s):
                ss = ss + str(count) + str(c)
            s = ss
            index += 1

        return s


if __name__ == '__main__':
    s = Solution()
    r = []
    for i in range(30):
        r.append(s.countAndSay(i+1))
    print r

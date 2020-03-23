class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ''

        p = strs[0]
        for s in strs:
            if len(s) < len(p):
                p = s

        i = 0
        while i < len(p):
            done = False
            for s in strs:
                if p[i] != s[i]:
                    done = True
                    break
            if done:
                break
            else:
                i += 1

        return p[0:i]


if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(["dog", "racecar", "car"])

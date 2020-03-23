class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        map = {}
        for ss in s:
            if ss not in map:
                map[ss] = 1
            else:
                map[ss] += 1

        for i in range(len(s)):
            if map[s[i]] == 1:
                return i

        return -1
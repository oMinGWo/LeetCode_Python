class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        map = {}
        for m in magazine:
            if m not in map:
                map[m] = 1
            else:
                map[m] += 1

        for r in ransomNote:
            if r not in map:
                return False
            elif map[r] == 0:
                return False
            else:
                map[r] -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print s.canConstruct('aac', 'ab')

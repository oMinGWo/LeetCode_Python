class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = set()
        max_length = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] not in ss:
                ss.add(s[j])
                j += 1
                max_length = max(max_length, j - i)
            else:
                ss.remove(s[i])
                i += 1

        return max_length


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring('pwwkew')

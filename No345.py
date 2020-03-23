class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        j = len(s) - 1
        a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ss = [cs for cs in s]
        while i < j:
            while i < len(s) and s[i] not in a:
                ss[i] = s[i]
                i += 1
            while j >= 0 and s[j] not in a:
                ss[j] = s[j]
                j -= 1
            if i == len(s) or j == -1:
                break
            ss[i] = s[j]
            ss[j] = s[i]
            i += 1
            j -= 1
        return ''.join(ss)


if __name__ == '__main__':
    s = Solution()
    print s.reverseVowels('.')

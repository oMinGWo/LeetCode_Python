class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isdigit() and not s[i].isalpha():
                i += 1
            while j >= 0 and not s[j].isdigit() and not s[j].isalpha():
                j -= 1
            if i == len(s) or j == -1:
                break
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('A man, a plan, a canal: Panama')

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if (x == '(' and c == ')') or (x == '[' and c == ']') or (x == '{' and c == '}'):
                    continue
                else:
                    return False

        return len(stack) == 0


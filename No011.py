class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        m = -1
        i = 0
        j = len(height) - 1
        while i < j:
            m = max(m, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m


if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

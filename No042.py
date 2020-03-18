class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 2:
            return 0

        hills = []
        for i in range(len(height)):
            if i == 0 and height[i] > height[i + 1]:
                hills.append(i)
            elif i == len(height) - 1 and height[-1] > height[-2]:
                while len(hills) > 1 \
                        and height[hills[-1]] <= height[i] \
                        and height[hills[-1]] <= height[hills[-2]]:
                    hills.pop()
                hills.append(i)
            elif i != len(height) - 1 and height[i - 1] <= height[i] and height[i] > height[i + 1] \
                    or height[i - 1] < height[i] and height[i] >= height[i + 1]:
                while len(hills) > 1 \
                        and height[hills[-1]] <= height[i] \
                        and height[hills[-1]] <= height[hills[-2]]:
                    hills.pop()
                hills.append(i)

        result = 0
        for i in range(len(hills) - 1):
            total = min(height[hills[i + 1]], height[hills[i]]) * (hills[i + 1] - hills[i])
            for j in range(hills[i], hills[i + 1]):
                total -= min(height[j], min(height[hills[i + 1]], height[hills[i]]))
            result += total
        return result


if __name__ == '__main__':
    s = Solution()
    print s.trap([6, 5, 2, 5, 6, 9, 1, 1])

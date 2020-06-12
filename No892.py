class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        total = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                n = grid[i][j]
                if n == 0:
                    continue
                total = total + 4 * n + 2
                if j - 1 >= 0:
                    total = total - 2 * min(grid[i][j], grid[i][j - 1])
                if i - 1 >= 0:
                    total = total - 2 * min(grid[i][j], grid[i - 1][j])

        return total


if __name__ == '__main__':
    s = Solution()
    print s.surfaceArea([[1, 0], [0, 2]])

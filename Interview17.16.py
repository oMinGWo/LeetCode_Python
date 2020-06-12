class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[-1][0], dp[-1][1])


if __name__ == '__main__':
    s = Solution()
    print s.massage([2, 1, 1, 2])

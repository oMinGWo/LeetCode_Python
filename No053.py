class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        m = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if sum < 0:
                sum = n
                m = max(sum, m)
            else:
                sum += n
                m = max(sum, m)
        m = max(sum, m)
        return m


if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-1, 0, -2])

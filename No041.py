class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums):
                n[nums[i] - 1] = nums[i]
        for i in range(len(n)):
            if n[i] != i + 1:
                return i + 1

        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([2, 2])

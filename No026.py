class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            len(nums)

        l = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[l]:
                nums[l + 1] = nums[i]
                l += 1

        return l + 1

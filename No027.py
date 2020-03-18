class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        l = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1

        return l

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == len(nums) - 1 or target < nums[mid + 1]:
                    return mid + 1
                else:
                    left = mid + 1
            else:
                if mid == 0 or target > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1


if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1, 3, 5, 6], -1)

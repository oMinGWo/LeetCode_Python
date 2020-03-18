def help(low, high, nums, target):
    if low > high:
        return -1
    mid = (low + high) / 2
    if nums[mid] == target:
        return mid

    if nums[mid] >= nums[low]:
        if nums[mid] > target >= nums[low]:
            return help(low, high - 1, nums, target)
        else:
            return help(low + 1, high, nums, target)
    elif nums[mid] < nums[high]:
        if nums[mid] < target <= nums[high]:
            return help(low + 1, high, nums, target)
        else:
            return help(low, high - 1, nums, target)
    else:
        return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        return help(0, len(nums) - 1, nums, target)


if __name__ == '__main__':
    s = Solution()
    print s.search([3, 1], 1)

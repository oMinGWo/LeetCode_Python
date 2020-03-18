def help(left, right, nums, target, isLeft):
    if left > right:
        return -1
    mid = (left + right) / 2
    if nums[mid] == target:
        if isLeft:
            if mid == 0 or nums[mid] > nums[mid - 1]:
                return mid
            else:
                right = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                return mid
            else:
                left = mid + 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    return help(left, right, nums, target, isLeft)


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        return [help(0, len(nums)-1, nums, target, True), help(0, len(nums)-1, nums, target, False)]


if __name__ == '__main__':
    s = Solution()
    print s.searchRange([1, 1], 1)

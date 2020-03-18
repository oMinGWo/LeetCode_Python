import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        min_minus = sys.maxint
        result = 0
        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == target:
                    return s
                elif s < target:
                    if target - s < min_minus:
                        min_minus = target - s
                        result = s
                    left += 1
                else:
                    if s - target < min_minus:
                        min_minus = s - target
                        result = s
                    right -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest([-4, -1, 1, 2], 1)

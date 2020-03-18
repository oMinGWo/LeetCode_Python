class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if left != i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right != len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -=1
                    continue
                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])

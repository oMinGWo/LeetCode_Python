class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for j in range(0, len(nums)):
            if j != 0 and nums[j] == nums[j - 1]:
                continue
            for i in range(j + 1, len(nums)):
                if i != j + 1 and nums[i] == nums[i - 1]:
                    continue

                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if left != i + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if right != len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    s = nums[left] + nums[right] + nums[i] + nums[j]
                    if s == target:
                        result.append([nums[i], nums[left], nums[right], nums[j]])
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print s.fourSum([1, 0, -1, 0, -2, 2], 0)

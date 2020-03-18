class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        k = len(nums) - 1
        index = 0
        while k >= 1:
            if nums[k] <= nums[k - 1]:
                k -= 1
            else:
                index = k
                break
        if index == 0:
            nums.sort()
            return

        fore_num = nums[index - 1]
        for i in range(index, len(nums)):
            if i == len(nums) - 1 or nums[i] > fore_num >= nums[i + 1]:
                t = nums[i]
                nums[i] = nums[index - 1]
                nums[index - 1] = t
                break

        t = []
        for i in range(index, len(nums)):
            t.append(nums[i])
        t.sort()
        for i in range(index, len(nums)):
            nums[i] = t[i - index]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 6, 7, 6, 3, 2]
    s.nextPermutation(nums)
    print nums

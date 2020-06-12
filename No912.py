class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        self.quickSort(0, len(nums) - 1, nums)
        return nums

    def swap(self, i, j, nums):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def quickSort(self, low, high, nums):
        if low > high:
            return
        i = low
        j = high - 1
        pivot = high
        while True:
            while 0 <= i < len(nums) and nums[i] < nums[pivot]:
                i += 1
            while 0 <= j < len(nums) and nums[j] >= nums[pivot]:
                j -= 1
            if i < j:
                self.swap(i, j, nums)
            else:
                break

        self.swap(i, pivot, nums)
        self.quickSort(low, i - 1, nums)
        self.quickSort(i + 1, high, nums)


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    s = Solution()
    print s.sortArray(nums)

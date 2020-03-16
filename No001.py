class Solution(object):
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        map = {}
        for i, v in enumerate(nums):
            map[v] = i

        for i, v in enumerate(nums):
            t = target - v
            if map.has_key(t) and map.get(t) != i:
                return [i, map.get(t)]


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([1, 2, 3, 3], 6)

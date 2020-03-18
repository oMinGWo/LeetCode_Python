class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        selected = []
        self.dfs(candidates,result, target, selected, 0)

        return result

    def dfs(self, nums, result, target, selected, si):
        if target == 0:
            s = selected[:]
            result.append(s)
            return

        for i in range(si, len(nums)):
            if nums[i] <= target:
                selected.append(nums[i])
                self.dfs(nums, result, target - nums[i], selected, i)
                selected.pop()


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2, 3, 5], 8)

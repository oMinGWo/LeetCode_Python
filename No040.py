class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        selected = []
        candidates.sort()
        self.dfs(candidates, result, target, selected, 0)

        return result

    def dfs(self, nums, result, target, selected, si):
        if target == 0:
            found = False
            selected.sort()
            for l in result:
                l.sort()
                if len(l) == len(selected):
                    found = True
                    for i in range(0, len(l)):
                        if l[i] != selected[i]:
                            found = False
                            break
                    if found:
                        return

            s = selected[:]
            result.append(s)
            return

        for i in range(si, len(nums)):
            if nums[i] <= target:
                selected.append(nums[i])
                self.dfs(nums, result, target - nums[i], selected, i + 1)
                selected.pop()


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([2, 5, 2, 1, 2], 5)

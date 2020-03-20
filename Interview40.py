class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        arr.sort()
        return arr[0:k]


if __name__ == '__main__':
    s = Solution()
    print s.getLeastNumbers([0, 1, 2, 1], 2)

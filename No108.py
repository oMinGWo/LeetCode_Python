# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from models import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        return self.help(0, len(nums)-1, nums)


    def help(self,left,right,nums):
        if left > right:
            return None

        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.help(left, mid - 1, nums)
        root.right = self.help(mid+1, right, nums)
        return root
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if q is None and p is None:
            return True
        if (q is None and p is not None) or (p is None and q is not None):
            return False
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

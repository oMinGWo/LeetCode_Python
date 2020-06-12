# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        return self.help(root.left, root.right)

    def help(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None or l.val != r.val:
            return False
        return self.help(l.left, r.right) and self.help(l.right, r.left)

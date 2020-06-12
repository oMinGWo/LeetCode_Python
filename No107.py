# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from models import TreeNode


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []
        if root is None:
            return result
        stack = [root]
        while len(stack) != 0:
            t = []
            tt = []
            for node in stack:
                t.append(node.val)
                if node.left is not None:
                    tt.append(node.left)
                if node.right is not None:
                    tt.append(node.right)
            stack = tt
            result.insert(0, t)
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print s.levelOrderBottom(root)

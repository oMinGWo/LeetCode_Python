# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from models import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        result = []
        n = root
        while len(stack) != 0 or n is not None:
            if n is not None:
                stack.append(n)
                n = n.left
            else:
                node = stack.pop()
                result.append(node.val)
                n = node.right

        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print s.inorderTraversal(root)






# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left = min(p.val, q.val)
        right = max(p.val, q.val)
        while root:
            if root.val > right: # greater than both
                root = root.left
            elif root.val < left: # less than both
                root = root.right
            else:
                return root
                
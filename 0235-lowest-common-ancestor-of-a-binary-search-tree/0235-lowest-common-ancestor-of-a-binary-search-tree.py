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
        left = p if p.val < q.val else q
        right = p if p.val > q.val else q
        while root:
            if root.val > right.val: # greater than both
                root = root.left
            elif root.val < left.val: # less than both
                root = root.right
            else:
                return root
                
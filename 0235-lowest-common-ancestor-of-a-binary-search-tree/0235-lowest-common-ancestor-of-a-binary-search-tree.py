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
        curr = root
        left = p if p.val < q.val else q
        right = p if p.val > q.val else q
        while True:
            
            if curr.val > right.val: # greater than both
                curr = curr.left
            elif curr.val < left.val: # less than both
                curr = curr.right
            else:
                return curr
                
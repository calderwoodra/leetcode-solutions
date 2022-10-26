# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def isValid(root, minVal, maxVal):
            # root = 5, left = 1, right = 4, min = -inf, max=+inf
            if root.left and (root.left.val >= root.val or root.left.val <= minVal):
                return False
            if root.right and (root.right.val <= root.val or root.right.val >= maxVal):
                return False
            
            right = left = True
            if root.left:
                # root = 1, min = -inf, max = 5
                left = isValid(root.left, minVal, root.val)
            
            if root.right:
                # root = 4, min = 5, max = +inf
                right = isValid(root.right, root.val, maxVal)
                
            return left and right
        return isValid(root, -sys.maxsize - 1, sys.maxsize)

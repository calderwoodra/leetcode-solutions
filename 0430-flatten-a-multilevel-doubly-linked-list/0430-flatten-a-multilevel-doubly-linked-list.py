"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        nodes = []
        
        def go_deeper(node):
            while node:
                nodes.append(node)
                go_deeper(node.child)
                node = node.next
        go_deeper(head)
        
        prev = None
        curr = nodes.pop(0)
        while curr:
            curr.prev = prev
            prev = curr
            
            curr.next = nodes.pop(0) if nodes else None
            curr.child = None
            
            curr = curr.next
        return head
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        orig_to_new = { None: None }
        curr = head
        while curr:
            orig_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node = orig_to_new[curr]
            node.next = orig_to_new[curr.next]
            node.random = orig_to_new[curr.random]
            curr = curr.next
        
        return orig_to_new[head]
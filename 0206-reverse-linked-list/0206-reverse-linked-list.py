# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        root = head = nodes.pop()
        while nodes:
            head.next = nodes.pop()
            head = head.next
        head.next = None
        return root
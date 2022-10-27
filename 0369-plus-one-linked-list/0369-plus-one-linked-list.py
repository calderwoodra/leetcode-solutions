# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return ListNode(1)
        
        def reverse(front):
            prev = None
            curr = front
            next = curr.next
            
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        head = reverse(head)
        curr = head
        prev = None
        while True:
            if not curr:
                prev.next = ListNode(1)
                break
            if curr.val == 9:
                curr.val = 0
                prev = curr
                curr = curr.next
            else:
                curr.val += 1
                break
        
        head = reverse(head)
        return head

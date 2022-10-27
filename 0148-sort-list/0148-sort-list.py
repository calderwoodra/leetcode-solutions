# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        nodes = defaultdict(list)
        curr = head
        while curr:
            nodes[curr.val].append(curr)
            curr = curr.next
        
        keys = sorted(nodes.keys())
        sorted_nodes = []
        while keys:
            dupes = nodes[keys.pop()]
            while dupes:
                sorted_nodes.append(dupes.pop())
        
        head = curr = sorted_nodes.pop()
        while sorted_nodes:
            curr.next = curr = sorted_nodes.pop()
        curr.next = None
        return head
            
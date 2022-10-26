# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        root = None
        if list1.val < list2.val:
            root = list1
            list1 = list1.next
        else:
            root = list2
            list2 = list2.next

        head = root
        while list1 or list2:
            if not list1:
                head.next = list2
                return root
            if not list2:
                head.next = list1
                return root
            
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        return root
    
# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        power_to_coeff_1 = defaultdict(int)
        power_to_coeff_2 = defaultdict(int)
        
        while poly1:
            power_to_coeff_1[poly1.power] = poly1.coefficient
            poly1 = poly1.next
        
        while poly2:
            power_to_coeff_2[poly2.power] = poly2.coefficient
            poly2 = poly2.next

        powers = set(power_to_coeff_1.keys() + power_to_coeff_2.keys())
        nodes = []
        for power in sorted(powers):
            coeff = power_to_coeff_1[power] + power_to_coeff_2[power]
            if coeff != 0:
                nodes.append(PolyNode(coeff, power))
        
        if not nodes:
            return None
        
        head = curr = nodes.pop()
        while nodes:
            curr.next = nodes.pop()
            curr = curr.next
        return head
            
        
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.curr = v1 if v1 else v2
        

    def next(self):
        """
        :rtype: int
        """
        result = self.curr.pop(0)
        if self.curr == self.v1:
            self.curr = self.v2 if self.v2 else self.v1
        else:
            self.curr = self.v1 if self.v1 else self.v2
        return result
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.curr) != 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) < len(s):
            return False
        elif len(t) == len(s):
            return t == s
        elif len(s) == 0:
            return True
        
        runner = 0
        for i, c in enumerate(t):
            if c == s[runner]:
                runner += 1
            
            if runner == len(s):
                return True
        return False
        
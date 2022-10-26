class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dups = set()
        seen = set()
        for i in range(len(s)):
            if i + 10 > len(s):
                break
            
            sub = s[i:i + 10]
            if sub in seen:
                dups.add(sub)
            else:
                seen.add(sub)
        
        return list(dups)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        
        longest = s[0]
        # Find the longest odd length
        for i in range(len(s)):
            padding = 1
            while True:
                if i - padding < 0:
                    break
                if i + padding >= len(s):
                    break
                if s[i - padding] != s[i + padding]:
                    break
                if 1 + padding * 2 > len(longest):
                    longest = s[i - padding:i + padding + 1]
                padding += 1
        
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                continue
            
            padding = 0
            while True:
                if i - padding < 0:
                    break
                if i + padding + 1 >= len(s):
                    break
                if s[i - padding] != s[i + 1 + padding]:
                    break
                if 2 + padding * 2 > len(longest):
                    longest = s[i - padding:i + 2 + padding]
                padding += 1
        return longest
                
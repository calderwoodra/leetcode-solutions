class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        n=1, output=1
        n=2, output=2
        n=3, output=3
        n=4, output=4 1,1,1,1 | 1,1,2 | 2,1,1 | 2,2
        n=5, output=7  1,1,1,1,1 | 1,1,1,2 | 1,2,1,1 | 2,1,1,1 | 2,2,1 | 2,1,2 | 1,2,2
        """
        
        memo = {0:1, 1:1}
        for i in range(2, n + 1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        
        
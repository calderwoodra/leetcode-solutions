class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        memo = {0: 0, 1: 1}
        for i in range(2, n + 1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
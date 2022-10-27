class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {0: cost[0], 1: cost[1]}
        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
        return min(memo[len(cost) - 1], memo[len(cost) - 2])
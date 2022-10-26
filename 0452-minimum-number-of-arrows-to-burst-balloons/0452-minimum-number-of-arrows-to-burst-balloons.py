class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        balloons = sorted(points, key=lambda p: p[1])
        ans, pos = 0, 0
        for [start, end] in balloons:
            if ans == 0 or start > pos:
                ans, pos = ans + 1, end
        return ans
            
        
        
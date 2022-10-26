class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current = 0
        result = []
        for num in nums:
            current += num
            result.append(current)
        return result
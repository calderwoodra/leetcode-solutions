class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        left = 0
        right = sum(nums) - nums[0]
        index = 0
        while index < len(nums) - 1:
            if left == right:
                return index
            
            left += nums[index]
            index += 1
            right -= nums[index]
            
        return index if left == right else -1

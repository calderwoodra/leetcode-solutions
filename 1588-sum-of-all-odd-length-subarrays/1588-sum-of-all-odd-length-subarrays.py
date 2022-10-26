class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = 1
        total = 0
        while l <= len(arr):
            i = 0
            while i + l <= len(arr):
                total += sum(arr[i:i+l])
                print(total, arr[i:i+l])
                i += 1
            l += 2
        return total
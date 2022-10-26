class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        top_half = defaultdict(int)
        for i in nums1:
            for j in nums2:
                top_half[i + j] += 1
        
        bottom_half = defaultdict(int)
        for i in nums3:
            for j in nums4:
                bottom_half[i + j] += 1

        count = 0
        for total, i in top_half.items():
            count += i * bottom_half[0 - total]
        return count
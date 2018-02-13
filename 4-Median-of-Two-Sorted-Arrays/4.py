class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = None
        nums = nums1+nums2
        nums = sorted(nums)
        median = nums[int((len(nums)-1)/2)] if len(nums)%2 == 1 else (nums[int(len(nums)/2-1)]+nums[int(len(nums)/2)])/2
        return median


nums1 = [1,3]
nums2 = [2]
print(Solution.findMedianSortedArrays(Solution.findMedianSortedArrays,nums1,nums2))
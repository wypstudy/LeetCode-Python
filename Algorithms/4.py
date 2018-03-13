# coding=utf-8


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge后排序，直接查中值
        # 由于是有序数列，理论上归并更快
        l = nums1
        l.extend(nums2)
        if len(l) == 0:
            return 0
        l.sort()
        index_median = len(l) / 2
        if len(l) % 2 == 0:
            return (l[index_median]+l[index_median-1])/2.0
        else:
            return l[index_median]


# test
instance = Solution()
print instance.findMedianSortedArrays([1, 3], [2, 4])
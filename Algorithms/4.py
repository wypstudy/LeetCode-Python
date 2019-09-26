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
        li = nums1
        li.extend(nums2)
        if len(li) == 0:
            return 0
        li.sort()
        index_median = int(len(li) / 2)
        if len(li) % 2 == 0:
            return (li[index_median]+li[index_median-1])/2.0
        else:
            return li[index_median]


# test
instance = Solution()
print(instance.findMedianSortedArrays([1, 3], [2, 4]))

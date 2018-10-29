# coding=utf-8


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        # 变成[(index,value)]格式
        nums = [(i, nums[i])for i in range(length)]
        # 根据value排序
        nums.sort(cmp=lambda x, y: cmp(x[1], y[1]))
        # 遍历两个数的组合
        i = 0
        j = 1
        while True:
            a = nums[i][1]
            b = nums[j][1]
            sumAB = a + b
            if sumAB == target:
                return [nums[i][0], nums[j][0]]
            j += 1
            # 当sumAB比target大时，后续不需要加了，直接换下一个a
            if j == length or sumAB > target:
                i += 1
                j = i + 1


# test
instance = Solution()
print(instance.twoSum(nums=[2, 5, 5, 11], target=10))


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
        nums = [(i, nums[i]) for i in range(length)]
        # 根据value排序
        nums.sort(key=lambda x: x[1])
        # 遍历两个数的组合
        i = 0
        j = 1
        while True:
            a = nums[i][1]
            b = nums[j][1]
            sum_ab = a + b
            if sum_ab == target:
                return [nums[i][0], nums[j][0]]
            j += 1
            # 当sumAB比target大时，后续不需要加了，直接换下一个a
            if j == length or sum_ab > target:
                i += 1
                j = i + 1


# test
instance = Solution()
print(instance.twoSum(nums=[11, 5, 2, 5], target=10))


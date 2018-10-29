# coding=utf-8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        answer = nums[0] + nums[1] + nums[2]
        for i in range(0, length - 2):
            left = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = length - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(three_sum - target) < abs(answer - target):
                    answer = three_sum
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return answer

instance = Solution()
print(instance.threeSumClosest([-1, 2, 1, -4], 1))


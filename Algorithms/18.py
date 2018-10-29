# coding=utf-8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        answer = []
        answer_prefix = []
        for i in range(0, length - 3):
            for j in range(i + 1, length - 2):
                if [nums[i], nums[j]] in answer_prefix:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        answer += [[nums[i], nums[j], nums[left], nums[right]]]
                        if [nums[i], nums[j]] not in answer_prefix:
                            answer_prefix += [[nums[i], nums[j]]]
                        while left < right and nums[left+1] == nums[left]:
                            left += 1
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                    if four_sum < target:
                        left += 1
                    else:
                        right -= 1

        return answer


instance = Solution()
print(instance.threeSumClosest([-3,-2,-1,0,0,1,2,3], 0))
print(instance.threeSumClosest([0,0,0,0], 0))


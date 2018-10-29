# coding=utf-8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        answer = set()
        for i in range(0, length - 2):
            left = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = length - 1
            sum = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] == sum:
                    answer.add("%d:%d:%d" % (nums[i], nums[left], nums[right]))
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                if sum - nums[left] - nums[right] > 0:
                    left += 1
                else:
                    right -= 1
        answer = list(answer)
        def func(x):
            xs = x.split(":")
            return map(lambda a: int(a), xs)
        return map(func, answer)



instance = Solution()
print(instance.threeSum([3,0,-2,-1,1,2]))
print(instance.threeSum([1,2,-2,-1]))
print(instance.threeSum([-1,0,1,2,-1,-4]))
print(instance.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

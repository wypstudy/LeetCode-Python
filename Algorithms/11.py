# coding=utf-8
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = area if area > max_area else max_area
            # 假设用dp,dp[i][j]表是i到j的最大容积,那么有
            # if height[a]<height[b]:
            #   dp[a][b]=max(height[a]*(b-a),dp[a+1][b])
            # else:
            #   dp[a][b]=max(height[b]*(b-a),dp[a][b-1])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


instance = Solution()
print(instance.maxArea([10,10,1,10]))
print(instance.maxArea([1,1]))

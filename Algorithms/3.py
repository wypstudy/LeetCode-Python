# coding=utf-8


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态转移方程
        # 设i为规划到的字符，s为原字符串，f[i]表示i位置为止(包括i)最长子串长度
        # 当s[i]与f[i-1]形成的最长子串无重复时
        #     f[i] = f[i-1] + 1
        # 当s[i]与f[i-1]形成的最长子串有重复时，设j为s[i]在 该子串中的位置 + 1
        #     f[i] = f[i-1] + 1 - j
        length = len(s)
        if length == 0:
            return 0
        max_len = 1
        dp = []
        for i in range(length):
            dp.append(0)
        dp[0] = 1
        for i in range(1, length):
            now_sub_str = s[i - dp[i - 1]:i]
            if s[i] not in now_sub_str:
                dp[i] = dp[i - 1] + 1
            else:
                j = now_sub_str.index(s[i]) + 1
                dp[i] = dp[i - 1] + 1 - j
            if dp[i] > max_len:
                max_len = dp[i]
        return max_len

# test
instance = Solution()
print(instance.lengthOfLongestSubstring("abcabcbb"))
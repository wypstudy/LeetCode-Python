# coding=utf-8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        str_length = len(s)
        p_length = len(p)

        # 把".*ab"分隔成['.*','a','b']
        pattern = []
        for i in range(p_length):
            if p[i].isalpha() or p[i] == '.':
                pattern.append(p[i])
            if p[i] == '*':
                pattern[-1] += '*'
        pattern_length = len(pattern)
        if pattern_length == 0:
            return str_length == 0

        # 设p为模式序列，s为要匹配的字符串
        # 设状态dp[i][j]表示p前i模式匹配s前j位的情况，有转移方程
        # dp[i][j] = True 当 i>0 且 j>0 且 dp[i-1][j-1] 且 p[i]能匹配s[j]
        #                 当 j>0 且 p[i]格式为'?*' 且 dp[i][j-1] 且 p[i]能匹配s[j]
        #                 当 i>0 且 p[i]格式为'?*' 且 dp[i-1][j]
        # 初始化 dp[0][0] = True 即空匹配空
        dp = [[False for j in range(str_length + 1)] for i in range(pattern_length + 1)]
        dp[0][0] = True

        def pattern_match(a, b):
            if len(a) == 1:
                if a == '.' or a == b:
                    return True
            if len(a) == 2:
                if a == '.*' or a[0] == b:
                    return True
            return False

        for i in range(1, pattern_length + 1):
            for j in range(str_length + 1):
                dp[i][j] = (j > 0 and dp[i-1][j-1] and pattern_match(pattern[i-1], s[j-1])) or \
                            (j > 0 and len(pattern[i-1]) == 2 and dp[i][j-1] and pattern_match(pattern[i-1], s[j-1])) or \
                            (len(pattern[i-1]) == 2 and dp[i-1][j])

        return dp[pattern_length][str_length]


# test
instance = Solution()
print instance.isMatch("aaa", "ab*ac*a")
print instance.isMatch("aab", "c*a*b")
print instance.isMatch("mississippi", "mis*is*p*.")
print instance.isMatch("mississippi", "mis*is*ip*.")


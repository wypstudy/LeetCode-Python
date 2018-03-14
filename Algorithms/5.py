# coding=utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # DP
        # f[x][y] = true 表示 s[x:y+1]为回文

        # 初始化
        left = 0
        right = 1
        length = len(s)
        f = [[False for j in range(length)] for i in range(length)]
        for i in range(length):
            # 单个字母是回文
            f[i][i] = True
            # 两个字母相同是回文，注意两个字母的回文答案
            if i < length - 1:
                if s[i] == s[i+1]:
                    f[i][i+1] = True
                    left = i
                    right = i + 2

        # j表示回文长度
        for j in range(3, length+1):
            # i表示回文起始坐标，则截止坐标为i+j-1
            for i in range(length-j+1):
                # f[x][y]为回文的需求是s[x]==s[y]并且f[x+1][y-1]=True
                if f[i + 1][i+j-1-1] and s[i] == s[i+j-1]:
                    f[i][i+j-1] = True
                    # 该DP后面的总是大于前面的，所以每次有答案就覆盖
                    left = i
                    right = i + j

        return s[left:right]


# test
instance = Solution()
print instance.longestPalindrome("babad")

# coding=utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 模拟即可，注意numRows为1的边界条件
        if numRows == 1:
            return s
        li = [[] for i in range(numRows)]
        t = 2 * numRows - 2
        for i in range(len(s)):
            j = i % t
            if j < numRows:
                li[j].append(s[i])
            else:
                li[t-j].append(s[i])
        re = ""
        for i in range(numRows):
            for c in li[i]:
                re += c
        return re

# test
instance = Solution()
print(instance.convert("PAYPALISHIRING", 3))

# coding=utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        # 取符号
        sign = -1 if s[0] == '-' else 1
        # 取数字
        number = s[1:len(s)] if s[0] == '-' else s
        # 反过来，并转成int
        number = int(number[::-1])
        # 如果数据大于2的31次方(32位有符号整数)，直接返回
        if number > pow(2, 31):
            return 0
        return sign * number

# test
instance = Solution()
print instance.reverse(123)
print instance.reverse(-120)

# coding=utf-8
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 打表
        thousand_digits = ['', 'M', 'MM', 'MMM']
        hundred_digits = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten_digits = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        digits = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        a = int(num / 1000)
        num = num % 1000
        b = int(num / 100)
        num = num % 100
        c = int(num / 10)
        d = num % 10
        roman = thousand_digits[a] + hundred_digits[b] + ten_digits[c] + digits[d]
        return roman


instance = Solution()
print(instance.intToRoman(1))
print(instance.intToRoman(4))
print(instance.intToRoman(9))
print(instance.intToRoman(49))
print(instance.intToRoman(1994))

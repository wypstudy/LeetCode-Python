# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 打表
        roman_map = {'': 0, 'M': 1000, 'MM': 2000, 'MMM': 3000,
                     'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800,
                     'CM': 900,
                     'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
                     'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9
                     }
        roman = list(s)
        i = 0
        length = len(roman)
        num = 0
        while i < length:
            if i < length - 1 and ''.join(roman[i:i+2]) in ['CD', 'CM', 'XL', 'XC', 'IV', 'IX']:
                num -= roman_map[roman[i]]
            else:
                num += roman_map[roman[i]]
            i += 1
        return num

instance = Solution()
print(instance.romanToInt("MCMXCIV"))

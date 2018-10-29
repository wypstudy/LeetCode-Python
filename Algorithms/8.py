class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number = 0
        try:
            length = len(str)
            start = 0
            while start < length and str[start] == ' ':
                start += 1
            end = start
            if str[end] == '-' or str[end] == '+':
                end += 1
            while end < length and str[end] in "0123456789":
                end += 1
            number = int(str[start:end])
        except Exception:
            pass
        if number > 2147483647:
            return 2147483647
        elif number < -2147483648:
            return -2147483648
        else:
            return number


# test
instance = Solution()
print(instance.myAtoi("-"))
print(instance.myAtoi(""))
print(instance.myAtoi("+120a23"))

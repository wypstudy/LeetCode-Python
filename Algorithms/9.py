class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if int(str(x)[::-1]) == x:
            return True
        return False
# test
instance = Solution()
print(instance.isPalindrome(-212))
print(instance.isPalindrome(1234321))
print(instance.isPalindrome(1211))

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            stack.append(c)
            if c in brackets.keys():
                if len(stack) > 1 and brackets[c] == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True


instance = Solution()
print(instance.isValid("[]"))
print(instance.isValid("[]()"))
print(instance.isValid("[({})]"))
print(instance.isValid("["))
print(instance.isValid("]"))
print(instance.isValid("[(]"))

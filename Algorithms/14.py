# coding=utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        re = ''
        index = 0
        while True:
            if index == len(strs[0]):
                return re
            now = strs[0][index]
            for s in strs:
                if index == len(s):
                    return re
                if s[index] != now:
                    return re
            re += now
            index += 1

instance = Solution()
print(instance.longestCommonPrefix(["flower","flow","flight"]))
print(instance.longestCommonPrefix(["flower","flow"]))
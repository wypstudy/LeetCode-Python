# coding=utf-8
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': 'abc', '3': 'def',
                 '4': 'ghi', '5': 'jkl', '6': 'mno',
                 '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer = []
        length = len(digits)
        if length == 0:
            return answer
        index = [0] * length
        while True:
            answer.append("".join([phone[digits[i]][index[i]] for i in range(length)]))
            c = length - 1
            while c >= 0:
                index[c] = (index[c] + 1) % len(phone[digits[c]])
                if index[c] == 0:
                    c -= 1
                else:
                    break
            if c < 0:
                break
        return answer


instance = Solution()
print(instance.letterCombinations("23"))

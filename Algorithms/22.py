class Solution:
    def generateParenthesis(self, n: int):
        # 搜索
        # left左括号剩余个数 right右括号剩余个数 s当前字符串
        # 剪枝 左括号后面只搜右括号 右括号后面只搜左括号
        def fun(left, right, s):
            if left == 0 and right == 0:
                return [s]
            answer = []
            if s == "" or (len(s) > 0 and s[-1] == ')'):
                for i in range(left):
                    count = i + 1
                    answer.extend(fun(left - count, right, s + '(' * count))
            if len(s) > 0 and s[-1] == '(':
                for i in range(right - left):
                    count = i + 1
                    answer.extend(fun(left, right - count, s + ')' * count))
            return answer
        return fun(n, n, "")


instance = Solution()

print(sorted(instance.generateParenthesis(4)))

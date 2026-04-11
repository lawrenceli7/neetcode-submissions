class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for string in tokens:
            if string == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(first + second)
            elif string == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif string == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            elif string == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(string))
        return stack[-1]

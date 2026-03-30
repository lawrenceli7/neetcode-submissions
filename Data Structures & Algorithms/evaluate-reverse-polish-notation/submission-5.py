class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                firstChar = stack.pop()
                secondChar = stack.pop()
                stack.append(secondChar + firstChar)
            elif char == "-":
                firstChar = stack.pop()
                secondChar = stack.pop()
                stack.append(secondChar - firstChar)
            elif char == "*":
                firstChar = stack.pop()
                secondChar = stack.pop()
                stack.append(secondChar * firstChar)
            elif char == "/":
                firstChar = stack.pop() 
                secondChar = stack.pop()
                stack.append(int(secondChar / firstChar))
            else:
                stack.append(int(char))
        return stack[-1]
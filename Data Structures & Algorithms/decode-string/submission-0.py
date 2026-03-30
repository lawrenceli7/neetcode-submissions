class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                currStr = ""
                while stack and stack[-1] != "[":
                    currStr = stack.pop() + currStr

                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append(int(digit) * currStr)
        return "".join(stack)
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for c in s:
            if c in matching:
                if stack and stack[-1] == matching[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
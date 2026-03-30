class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingBracket = { "}" : "{", "]" : "[", ")" : "("}

        for char in s:
            if char in matchingBracket:
                if stack and stack[-1] == matchingBracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
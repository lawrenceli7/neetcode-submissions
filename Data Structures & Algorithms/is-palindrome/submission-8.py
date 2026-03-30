class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for char in s:
            if self.alphaNum(char):
                newStr += char.lower()
        return newStr == newStr[::-1]

    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))




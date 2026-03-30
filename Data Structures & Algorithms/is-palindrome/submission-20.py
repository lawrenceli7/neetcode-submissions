class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not self.isAlpha(s[left]) and left < right:
                left += 1
        
            while not self.isAlpha(s[right]) and right > left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True

    def isAlpha(self, c):
        return (ord("a") <= ord(c) <= ord("z") or 
        ord("A") <= ord(c) <= ord("Z") or
        ord("0") <= ord(c) <= ord("9"))
        

        



        
        




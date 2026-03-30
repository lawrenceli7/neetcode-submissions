class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1

        def isPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return (isPali(left + 1, right) or isPali(left, right - 1))

            left += 1
            right -= 1
        return True
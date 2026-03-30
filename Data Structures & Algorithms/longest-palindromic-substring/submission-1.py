class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            left, right = i, i # center postion
            # inbounds and is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # check length of palindrom
                if (right - left + 1) > resLen:
                    # update res
                    res = s[left:right+1]
                    # update res length
                    resLen = right - left + 1
                # update pointers
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        return res





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        numSet = set()
        res = 0

        for right in range(len(s)):
            while s[right] in numSet:
                numSet.remove(s[left])
                left += 1
            numSet.add(s[right])
            res = max(res, right - left + 1)
        return res
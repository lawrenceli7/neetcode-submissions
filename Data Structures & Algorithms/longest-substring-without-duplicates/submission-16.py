class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        res = left = 0

        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
            visit.add(s[right])
            res = max(res, right - left + 1)
        return res
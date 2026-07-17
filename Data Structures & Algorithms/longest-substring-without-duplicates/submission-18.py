class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        visit = set()

        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1

            visit.add(s[right])
            res = max(res, right - left + 1)
        return res
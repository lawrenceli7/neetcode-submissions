class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count the number of occurrences of each character
        # length of the window - count of most freq character = the number of characters we want to replace (needs to be <= k)

        count = {}
        res = 0
        left = 0
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res






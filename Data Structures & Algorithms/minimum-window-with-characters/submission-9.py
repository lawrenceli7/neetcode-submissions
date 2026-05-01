class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        for char in t:
            countT[char] += 1

        formed, total = 0, len(countT)
        left = 0
        res = float("inf")
        subLeft = subRight = 0

        for right in range(len(s)):
            char = s[right]
            if char in countT:
                countT[char] -= 1
                if countT[char] == 0:
                    formed += 1
            while left <= right and formed == total:
                length = right - left + 1
                if length < res:
                    res = length
                    subLeft, subRight = left, right + 1
                char = s[left]
                if char in countT:
                    if countT[char] == 0:
                        formed -= 1
                    countT[char] += 1
                left += 1
        return "" if res == float("inf") else s[subLeft: subRight]

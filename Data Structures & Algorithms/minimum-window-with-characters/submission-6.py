class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = Counter()
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left: right + 1] if resLen != float("inf") else ""
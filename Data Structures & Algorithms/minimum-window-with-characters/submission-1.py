class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = Counter(t)
        window = Counter()

        have = 0
        need = len(countT)
        left = 0
        res = [-1, -1]
        resLen = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                # update our result
                if (right - left + 1) < resLen:
                    # the window
                    res = [left, right]
                    # the size of window
                    resLen = right - left + 1
                 
                # keep shrinking from the left
                window[s[left]] -= 1
                if c in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right + 1] if resLen != float("inf") else ""







        
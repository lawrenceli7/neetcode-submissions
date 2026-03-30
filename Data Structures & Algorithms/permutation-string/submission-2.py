class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        s2Count = Counter(s2[:len(s1)])

        if s1Count == s2Count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            s2Count[s2[right]] += 1
            s2Count[s2[left]] -= 1
            left += 1

            if s2Count == s1Count:
                return True
        return False
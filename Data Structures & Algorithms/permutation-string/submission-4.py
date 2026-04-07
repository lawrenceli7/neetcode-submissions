class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = Counter(s1)
        countS2 = Counter(s2[:len(s1)])

        if countS1 == countS2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            countS2[s2[right]] += 1
            countS2[s2[left]] -= 1
            left += 1

            if countS1 == countS2:
                return True
        return False


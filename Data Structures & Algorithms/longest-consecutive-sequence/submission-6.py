class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        charSet = set(nums)
        longest = 0

        for num in charSet:
            if num - 1 not in charSet:
                length = 1
                while num + length in charSet:
                    length += 1
                longest = max(longest, length)
        return longest
        


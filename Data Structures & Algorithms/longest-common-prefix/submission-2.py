class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        # go through every char in prefix
        for i in range(len(prefix)):
            # check it with every string
            for s in strs:
                # if you reach to the end of the string or the chars do not match now
                if i == len(s) or s[i] != prefix[i]:
                    # return the prefix up until that point
                    return prefix[:i]
        return prefix
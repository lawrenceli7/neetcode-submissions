class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            sort = "".join(sorted(s))
            count[sort].append(s)
        return list(count.values())





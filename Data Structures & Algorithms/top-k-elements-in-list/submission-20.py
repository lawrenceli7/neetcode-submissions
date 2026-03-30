class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, cnt in count.items():
            arr.append([cnt, num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        
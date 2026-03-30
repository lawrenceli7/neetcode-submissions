class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        arr = []
        for n, cnt in count.items():
            arr.append([cnt, n])
        arr.sort()

        res = []
        for i in range(len(arr) - 1, len(arr) - k - 1, -1):
            res.append(arr[i][1])
        return res
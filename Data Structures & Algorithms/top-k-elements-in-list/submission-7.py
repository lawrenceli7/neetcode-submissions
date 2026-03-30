class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, map count to values
        # key: i (count), value: the list of values that occurred
        # the max num of occurrences of a value is the length of the array
        # count the number of occurrences of each element in the array
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

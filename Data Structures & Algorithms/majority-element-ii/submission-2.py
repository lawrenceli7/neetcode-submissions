class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for n in count:
            if count[n] > len(nums) // 3:
                res.append(n)
        return res
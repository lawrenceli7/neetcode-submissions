class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        visit = set()
        total = sum(nums) // k
        if sum(nums) / k != total:
            return False


        def backtracking(i, subsetLeft, subsetSum):
            if subsetLeft == 0:
                return True

            if subsetSum == total:
                return backtracking(0, subsetLeft - 1, 0)
            
            prev = -1
            for j in range(i, len(nums)):
                if j in visit or subsetSum + nums[j] > total:
                    continue
                if nums[j] == prev:
                    continue
                
                visit.add(j)
                if backtracking(j + 1, subsetLeft, subsetSum + nums[j]):
                    return True
                visit.remove(j)
                prev = nums[j]
            return False
        return backtracking(0, k, 0)
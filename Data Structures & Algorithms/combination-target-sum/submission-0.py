class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # need to elimate duplicates, recursive decision tree

        res = []

        # i (which nums we are still allowed to choose)
        # curr (a list to tell which vals we added to the current combination)
        # total (maintain the total sum of vals in curr)
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            # out of bounds
            if i >= len(nums) or total > target:
                return
            
            # include nums
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # not include nums
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


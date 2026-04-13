class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # contains index
        left = 0
        res = []

        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove left value from window
            if left > q[0]:
                q.popleft()

            # update size of window
            if (right - left + 1) >= k:
                res.append(nums[q[0]])
                left += 1

            right += 1
        return res
            
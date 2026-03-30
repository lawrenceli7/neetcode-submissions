class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        left, right = 0, len(people) - 1

        while left <= right:
            remain = limit - people[right]
            right -= 1
            boats += 1
            if left <= right and remain >= people[left]:
                left += 1
        return boats
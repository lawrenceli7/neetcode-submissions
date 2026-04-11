class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        slow_car = 0

        for p, s in sorted(zip(position, speed), reverse = True):
            eta = (target - p) / s
            if eta > slow_car:
                res += 1
                slow_car = eta
        return res
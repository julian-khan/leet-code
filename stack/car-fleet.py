# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [(position[i], speed[i]) for i in range(len(position))]
        posAndSpeed.sort(reverse=True)

        stack = []
        for pos, spd in posAndSpeed:
            if stack:
                t1 = (target - pos) / spd

                p2, s2 = stack[-1]
                t2 = (target - p2) / s2

                if t1 <= t2:
                    continue
            stack.append((pos, spd))
            

        return len(stack)

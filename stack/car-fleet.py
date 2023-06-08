# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [(position[i], speed[i]) for i in range(len(position))]
        posAndSpeed.sort(reverse=True)

        stack = []
        for pos, spd in posAndSpeed:
            time = (target - pos) / spd #speed = distance / time formula
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
            
        return len(stack)

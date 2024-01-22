from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Purpose: return asteroid after collsion
        # Method: stacks
        # Intuititon: check collion cases (a or stack[-1] is stronger)
        stack = []
        for incoming_asteroid in asteroids:
            while len(stack) > 0 and incoming_asteroid < 0 and stack[-1] > 0:
                # If coming one is negative and sitting one is positive then a collision can happen
                if stack[-1] > abs(incoming_asteroid):
                    incoming_asteroid = 0
                    # It is less poweful and the asteroid is only added if it is negative or positive and not zero
                elif stack[-1] < abs(incoming_asteroid):
                    stack.pop()
                    # Coming asteroid is more powerful than the sitting one
                else:
                    # Both are equal
                    stack.pop()
                    incoming_asteroid = 0
            if incoming_asteroid > 0 or incoming_asteroid < 0:
                stack.append(incoming_asteroid)
        return stack
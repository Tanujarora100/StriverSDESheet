from typing import List


class Solution(object):
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Purpose: return asteroid after collsion
        # Method: stacks
        # Intuititon: check collion cases (a or stack[-1] is stronger)
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                dif = a + stack[-1]
                # a is stronger
                if dif < 0:
                    stack.pop()
                # stack[-1] is stronger
                elif dif > 0:
                    break
                # equal
                else:
                    stack.pop()
                    break
            # no collision
            else:
                stack.append(a)
        return stack
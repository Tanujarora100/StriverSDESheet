from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
       #Whenever you see something related to rotation try to think of a deque
    #By appending something and removing somethin
        if s==goal:
            return True
        deq_one= deque(s)
        deq_two=deque(goal)
        i=0
        while i<len(s):
            deq_one.append(deq_one.popleft())
            if deq_two==deq_one:
                return True
            i=i+1
        return False
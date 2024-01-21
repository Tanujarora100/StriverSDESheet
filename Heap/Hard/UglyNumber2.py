from heapq import heapify, heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heaped=[1]
        heapify(heaped)
        set_val=set([1])
        result=1
        while n:
            top=heappop(heaped)
            result=top
            if top*2 not in set_val:
                heappush(heaped,top*2)
                set_val.add(top*2)
            if top*3 not in set_val:
                heappush(heaped,top*3)
                set_val.add(top*3)
            if top*5 not in set_val:
                heappush(heaped,top*5)
                set_val.add(top*5)
            n-=1
            
        return result
        
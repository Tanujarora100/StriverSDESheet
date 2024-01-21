import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        f = [0] * 26
        n = len(s)
        
        for char in s:
            f[ord(char) - ord('a')] += 1
            if f[ord(char) - ord('a')] > (n + 1) // 2:
                return ""
        
        pq = [(-freq, chr(char + ord('a'))) for char, freq in enumerate(f) if freq != 0]
        heapq.heapify(pq)
        
        ans = []
        while len(pq) >= 2:
            freq1, char1 = heapq.heappop(pq)
            freq2, char2 = heapq.heappop(pq)
            ans.extend([char1, char2])
            
            if freq1 < -1:
                heapq.heappush(pq, (freq1 + 1, char1))
            if freq2 < -1:
                heapq.heappush(pq, (freq2 + 1, char2))
        
        if pq:
            ans.append(pq[0][1])
        
        return "".join(ans)

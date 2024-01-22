from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        q=deque()
        dominoes=list(dominoes)
        for a,i in enumerate(dominoes):
            if i=="L"or i=="R":
                q.append((i,a))
                
        # print(q)
                
        while(q):
            val,ind=q.popleft()
            
            if val=="R" and ind+1<len(dominoes) and dominoes[ind+1]==".":
                if q and q[0][0]=="L" and ind+2==q[0][1]:
                    q.popleft()
                else:
                    dominoes[ind+1]="R"
                    q.append(("R",ind+1))
                    
                    
            elif val=="L" and ind>0 and dominoes[ind-1]==".":
                dominoes[ind-1]="L"
                q.append(("L",ind-1))
                
        return "".join(dominoes)
                
            
            
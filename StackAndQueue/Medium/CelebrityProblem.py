#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        stack=[]
        
        for i in range(n):
            stack.append(i)
        
        
        while len(stack)!=1:
            a= stack.pop()
            b=stack.pop()
            if self.knows(a,b,M):
                stack.append(b)
            else:
                stack.append(a)
        candidate= stack[-1]
        
        
        #Verify now
        row_check=False
        zeroCount=0
        for i in range(n):
            if M[candidate][i]==0:
                zeroCount+=1
        if zeroCount!=n:
            return -1
        
        one_count=0
        col_check=False
        for i in range(n):
            if M[i][candidate]==1:
                one_count+=1
        if one_count!=n-1:
            return -1
        
        return candidate
    
    def knows(self,a,b,M):
        if M[a][b]==1:
            return True
        else:
            return False
            


from queue import LifoQueue
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        # create stack to store leaders
        sk = []
        leaders=[]
        sk.append(A[N - 1])
        for i in range(N - 2, -1, -1):
            if(A[i] >= sk[len(sk) - 1]):
                sk.append(A[i])
     
        # print stack elements
        # run loop till stack is not empty
        while(len(sk) != 0):
            leaders.append(sk.pop())
        return leaders
 
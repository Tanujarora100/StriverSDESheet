
class Solution:
    def guessNumber(self, n: int) -> int:
        start=1
        # Start is 1 because numbers are starting from 1 to n
        end=n
        while start<=end:
            mid=start+(end-start)//2
            #Same as Binary search just this time they are giving us the target through the guess api.
            if guess(mid)==0:
                #If Number is exactly the same then just return the mid index.
                return mid
            #Higher Number search left side of array
            elif guess(mid)==-1:
                end=mid-1
            #Lower Number then search right side of array
            else:
                start=mid+1
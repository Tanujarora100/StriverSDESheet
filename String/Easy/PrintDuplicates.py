# Python3 program to count all duplicates
# from string using maps
def printDups(Str):
 
    count = {}
    for i in range(len(Str)):
        if(Str[i] in count):
            count[Str[i]] += 1
        else:
            count[Str[i]] = 1
        #increase the count of characters by 1 
  
    for it,it2 in count.items():  #iterating through the unordered map 
        if (it2 > 1):   #if the count of characters is greater than 1 then duplicate found
            print(str(it) + ", count = "+str(it2))
     
# Driver code
Str = "test string"
printDups(Str)
from collections import Counter, defaultdict
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hash_map= Counter(needle)
        main_map= defaultdict(int)
        i=0
        j=0
        k=len(needle)
        prefix=""
        while j<len(haystack):
            prefix+=haystack[j]
            main_map[haystack[j]]+=1
            if j-i+1<k:
                j=j+1
            elif j-i+1==k:
                if prefix==needle:
                    return i
                else:
                    prefix= prefix[1:]
                    main_map[haystack[i]]-=1
                    if main_map[haystack[i]]==0:
                        del main_map[haystack[i]]
                    i+=1
                    j+=1
        return -1
                    
                
    
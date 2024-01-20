from typing import List

from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict to store lists of anagrams
        anagram_groups = defaultdict(list)
        
        # Iterate through each string in the input list
        for curr_string in strs:
            # Create a list of 26 zeros to represent the count of each character in the string
            char_count = [0] * 26
            
            # Count the occurrences of each character in the current string
            for char in curr_string:
                char_count[ord(char) - ord('a')] += 1
            
            # Convert the list of character counts to a tuple to use as a key in the defaultdict
            key = tuple(char_count)
            
            # Append the current string to the list of anagrams for the corresponding key
            anagram_groups[key].append(curr_string)
        
        # Return a list of all the lists of anagrams
        return list(anagram_groups.values())

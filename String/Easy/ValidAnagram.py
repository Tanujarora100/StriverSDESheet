class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrayOne = [0] * 26
        arrayTwo = [0] * 26

        for char in s:
            arrayOne[ord(char) - ord('a')] += 1

        for char in t:
            arrayTwo[ord(char) - ord('a')] += 1

        return arrayOne == arrayTwo
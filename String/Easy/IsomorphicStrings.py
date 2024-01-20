class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = [0] * 200
        map2 = [0] * 200

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if map1[ord(s[i])] != map2[ord(t[i])]:
                return False

            map1[ord(s[i])] = i + 1
            map2[ord(t[i])] = i + 1

        return True

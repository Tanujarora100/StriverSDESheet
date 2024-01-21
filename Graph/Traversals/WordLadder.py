from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # T: O(nm^2), S: O(nm), n = len(word_list), m = len(word)
        word_set=set(wordList)
        if endWord not in word_set:
            return 0
        ans=self.bfs(beginWord,endWord,wordList)
        return ans
        
        
    def bfs(self,beginWord, endWord,wordList):
        word_set = set(wordList)
        seen = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            lvl_sz = len(queue)
            for _ in range(lvl_sz):
                curr = queue.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    for ch in range(ord('a'), ord('z') + 1):
                        curr_list = list(curr)
                        curr_list[i] = chr(ch)
                        new_curr = ''.join(curr_list)
                        if new_curr in word_set and new_curr not in seen:
                            queue.append(new_curr)
                            seen.add(new_curr)
            res += 1
        return 0
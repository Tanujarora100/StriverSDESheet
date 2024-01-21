import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.user = defaultdict(set)
        self.tweet = defaultdict(list)
        self.n = 0

        for i in range(1, 501):
            self.user[i] = set()
            self.tweet[i] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([tweetId, self.n])
        self.n += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        heap.extend(self.tweet[userId])
        for i in self.user[userId]:
            heap.extend(self.tweet[i])

        heap.sort(key=lambda x: x[1], reverse=True)

        count = 1
        result = []
        while heap and count <= 10:
            temp = heap.pop(0)
            result.append(temp[0])
            count += 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId].discard(followeeId)

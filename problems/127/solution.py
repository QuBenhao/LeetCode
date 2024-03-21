import solution
import string
from collections import deque
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.ladderLength(*test_input)

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        class Queue:
            def __init__(self):
                self.queue = deque([])
                self.explored = dict()

            def __contains__(self, item):
                return item in self.explored

            def __add__(self, other):
                self.queue.append(other[1])
                self.explored[other[1]] = other[0]

            def __len__(self):
                return len(self.queue)

            def pop(self):
                return self.queue.popleft()

        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        front, back = Queue(), Queue()
        front.__add__((1, beginWord))
        back.__add__((1, endWord))
        while front and back:
            if len(front) > len(back):
                ts, ot = back, front
            else:
                ts, ot = front, back
            s = ts.pop()
            for i in range(len(s)):
                for c in string.ascii_lowercase:
                    t = s[:i] + c + s[i + 1:]
                    if t in wordList and t not in ts:
                        if t in ot:
                            return ts.explored[s] + ot.explored[t]
                        ts.__add__((ts.explored[s] + 1, t))
        return 0

        # def heuristic(curr, target):
        #     return sum(1 for a, b in zip(curr, target) if a != b)
        #
        # wordList = set(wordList)
        # if endWord not in wordList:
        #     return 0
        # pq = [(0, 0, beginWord)]
        # costs = {beginWord:0}
        # while pq:
        #     _, g, s = heapq.heappop(pq)
        #     if s == endWord:
        #         return g + 1
        #     for i in range(len(s)):
        #         for c in string.ascii_lowercase:
        #             t = s[:i] + c + s[i + 1:]
        #             if t in wordList and (t not in costs or costs[t] > g + 1):
        #                 costs[t] = g + 1
        #                 heapq.heappush(pq, (heuristic(t, endWord) + g + 1, g + 1, t))
        # return 0

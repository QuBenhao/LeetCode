import solution
import string
from collections import deque
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        beginWord, endWord, wordList = test_input
        return self.ladderLength(beginWord, endWord, list(wordList))

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

        # class ProirtyQueue:
        #     def __init__(self):
        #         self.queue = []
        #         self.explored = dict()
        #
        #     def __contains__(self, item):
        #         return item in self.explored
        #
        #     def __add__(self, other):
        #         heapq.heappush(self.queue, other)
        #         self.explored[other[2]] = other[0]
        #
        #     def __len__(self):
        #         return len(self.queue)
        #
        #     def pop(self):
        #         return heapq.heappop(self.queue)
        #
        # def heuristic(curr, target):
        #     return sum(1 for a, b in zip(curr, target) if a != b)
        #
        # wordList = set(wordList)
        # if endWord not in wordList:
        #     return 0
        # front = ProirtyQueue()
        # front.__add__((1, 0, beginWord))
        # while front:
        #     l, _, s = front.pop()
        #     if s == endWord:
        #         return l
        #     for i in range(len(s)):
        #         for c in string.ascii_lowercase:
        #             t = s[:i] + c + s[i + 1:]
        #             if t in wordList and t not in front:
        #                 front.__add__((l + 1, heuristic(t, endWord), t))
        # return 0

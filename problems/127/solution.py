import solution
import string
from collections import deque


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
                self.queue.append(other)
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
            length, s = ts.pop()
            for i in range(len(s)):
                for c in string.ascii_lowercase:
                    t = s[:i] + c + s[i + 1:]
                    if t in wordList and t not in ts:
                        if t in ot:
                            return length + ot.explored[t]
                        ts.__add__((length + 1, t))
        return 0

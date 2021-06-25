import solution
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        deadends, target = test_input
        return self.openLock(list(deadends), target)

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        class Queue:
            def __init__(self):
                self.queue = deque([])
                self.cost = dict()

            def __contains__(self, item):
                return item in self.cost

            def __len__(self):
                return len(self.queue)

            def add(self, item):
                self.queue.append(item[1])
                self.cost[item[1]] = item[0]

            def pop(self):
                return self.queue.popleft()

            # update function
            def update(self, other, constraint=None):
                s = self.pop()
                cost = self.cost[s]
                for successor in action(s):
                    if successor not in self and (not constraint or successor not in constraint):
                        if successor in other:
                            return cost + other.cost[successor]
                        self.add((cost + 1, successor))
                return -1

        # transition function
        def action(string):
            return [string[:i] + str((int(c) + d) % 10) + string[i + 1:] for d in (-1, 1) for i, c in enumerate(string)]

        init = "0000"
        if target == init:
            return 0
        deadends = set(deadends)
        if init in deadends:
            return -1
        front, back = Queue(), Queue()
        front.add((0, init))
        back.add((1, target))
        while front and back:
            if len(front) > len(back):
                res = back.update(front, deadends)
            else:
                res = front.update(back, deadends)
            if res != -1:
                return res
        return -1

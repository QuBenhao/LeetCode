import solution
from sortedcontainers import SortedDict, SortedList


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSkyline(list(x[:] for x in test_input))

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # ans = []
        # changes = []
        # for left, right, height in buildings:
        #     changes.append((left, -height))
        #     changes.append((right, height))
        # changes.sort()
        # lives = SortedDict()
        # lives[0] = 1
        # for x, h in changes:
        #     # Add a building
        #     if h < 0:
        #         if h in lives:
        #             lives[h] += 1
        #         else:
        #             lives[h] = 1
        #             # Tallest building
        #             if h == lives.keys()[0]:
        #                 ans.append([x, -h])
        #     # Remove a building
        #     else:
        #         lives[-h] -= 1
        #         if not lives[-h]:
        #             lives.pop(-h)
        #             # Check whether the tallest building has changed
        #             new_max = lives.keys()[0]
        #             if -new_max < h:
        #                 ans.append([x, -new_max])
        # return ans

        ans = []
        changes = []
        for left, right, height in buildings:
            changes.append((left, -height))
            changes.append((right, height))
        # Sort the change events by position
        changes.sort()
        # Likewise, include a default height of 0
        lives = SortedList([0])
        # Previous maximum building height
        prev = 0
        for x, h in changes:
            # Add or remove a building according to h
            if h < 0:
                lives.add(h)
            else:
                lives.remove(-h)
            # Current maximum height after the addition or removal
            curr_max = -lives[0]
            # The maximum height has changed
            if curr_max != prev:
                ans.append([x, curr_max])
            prev = curr_max
        return ans

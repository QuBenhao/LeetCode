from collections import deque
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCandies(*test_input)

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque([])
        has_keys = set()
        has_boxes = set()
        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                has_boxes.add(box)
        ans = 0
        while q:
            box = q.popleft()
            ans += candies[box]
            for key in keys[box]:
                if key in has_boxes:
                    has_boxes.remove(key)
                    q.append(key)
                has_keys.add(key)
            for b in containedBoxes[box]:
                if status[b] == 1 or b in has_keys:
                    if b in has_keys:
                        has_keys.remove(b)
                    q.append(b)
                else:
                    has_boxes.add(b)
        return ans


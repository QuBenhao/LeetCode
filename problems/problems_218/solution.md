# [Python] Traverse building start and end events and record the maximum height at each change

> Author: Benhao
> Date: 2021-07-13
> Upvotes: 25
> Tags: Python, Python3

---

### Approach
The skyline can change only at the left and right edges of buildings. Use a min-heap to record each change, ordered by x coordinate: a negative height adds a building, and a positive height removes one. (Alternatively, collect all events and sort them.)

If a newly added building is the tallest, the skyline changes.
Similarly, if removing a building reduces the maximum height, the skyline changes.
To track the tallest active building at each point, I used SortedDict as a Counter. SortedList also works directly without counting how many buildings have each height; just check whether the maximum height changes.

### Code
Maintain heights with SortedDict
```python3
from sortedcontainers import SortedDict


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        changes = []
        for left, right, height in buildings:
            # Add the building at its left edge
            heapq.heappush(changes, (left, -height))
            # Remove the building at its right edge
            heapq.heappush(changes, (right, height))
        lives = SortedDict()
        # Always keep at least one building at ground level (imagine a height-0 building from 0 to inf)
        lives[0] = 1
        while changes:
            # Current position and height
            x, h = heapq.heappop(changes)
            # Add a building
            if h < 0:
                if h in lives:
                    lives[h] += 1
                else:
                    lives[h] = 1
                    # Tallest building
                    if h == lives.keys()[0]:
                        ans.append([x, -h])
            # Remove a building
            else:
                lives[-h] -= 1
                # No buildings of height -h remain
                if not lives[-h]:
                    lives.pop(-h)
                    # Check whether the tallest building has changed
                    new_max = lives.keys()[0]
                    if -new_max < h:
                        ans.append([x, -new_max])
        return ans
```
Maintain heights with SortedList
```python3
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
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
```

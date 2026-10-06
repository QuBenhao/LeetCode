# From binary search to a single pass

> Author: Benhao
> Date: 2026-04-15
> Upvotes: 1
> Tags: Python3

---

> Problem: [3488. 距离最小相等元素查询](https://leetcode.cn/problems/closest-equal-element-queries/description/)

[TOC]

# Intuition

This problem has three approaches, from the most straightforward to the optimal:

1. **Method 1: Binary search** - The most straightforward approach: preprocessing + binary search
2. **Method 2: Two-pointer scan** - A single pass, but with larger constant factors
3. **Method 3: Precompute a distance array** - The optimal approach, with O(n+m) time complexity

# Solution steps

## Method 1: Binary search

**Core idea**: Precompute all positions of each value as a sorted list. For each query, use binary search to find the nearest positions on the left and right.

**Steps**:
1. Use a dictionary to record all positions of each value; they are naturally sorted
2. For query position `q`, find the position list for `nums[q]`
3. Use `bisect_left` to locate `q` in the list
4. Compare the distances to the neighboring positions on the left and right, and take the minimum
5. Handle the circular array separately: add `n` when calculating the distance across the end and beginning

```Python3 []
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # Preprocess: record all positions of each value
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = []
        for q in queries:
            positions = pos[nums[q]]
            if len(positions) == 1:
                ans.append(-1)
                continue
            
            min_dist = n
            # Use binary search to locate q in positions
            idx = bisect_left(positions, q)
            
            # Check the left side
            if idx > 0:
                min_dist = min(min_dist, q - positions[idx - 1])
            # Check the right side
            if idx < len(positions):
                min_dist = min(min_dist, positions[idx] - q)
            # Check the circular distance
            min_dist = min(min_dist, 
                          positions[0] + n - q,  # Wrap around the end
                          positions[-1] - q if positions[-1] <= q else q + n - positions[-1])
            
            ans.append(min_dist)
        
        return ans
```

## Method 2: Two-pointer scan

**Core idea**: Traverse the array twice to simulate a circular array, track the last position of each value, and update the answers.

**Steps**:
1. Use `query_map` to record the answer indices corresponding to each query position
2. Traverse `nums + nums` to simulate the circular array
3. At each position, update the answers for this position and the previous position with the same value
4. Finally, handle answers that were never updated (no other element has the same value)

```Python3 []
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        query_map = defaultdict(list)
        for i, q in enumerate(queries):
            query_map[q].append(i)
        
        ans = [n] * len(queries)
        last_idx = defaultdict(lambda: -n)
        
        for i, num in enumerate(nums + nums):
            if i % n in query_map:
                for j in query_map[i % n]:
                    ans[j] = min(ans[j], i - last_idx[num])
            if last_idx[num] % n in query_map:
                for j in query_map[last_idx[num] % n]:
                    ans[j] = min(ans[j], i - last_idx[num])
            last_idx[num] = i
        
        return [v if v < n else -1 for v in ans]
```

**Drawbacks**:
- `nums + nums` creates a new array, adding overhead
- The modulo operation `i % n` is expensive
- Although the nested loops perform O(m) iterations in total, the constant factor is large

## Method 3: Precompute a distance array (optimal)

**Core idea**: Precompute the distance from each position to the nearest element with the same value, then answer each query in O(1).

**Steps**:
1. Preprocess: use a dictionary to record all positions of each value
2. For each value's position list, calculate the distances from each position to its left and right neighbors
3. Handle wrapping separately: the first and last positions in the list require distances across the array boundary
4. Return the precomputed result directly for each query

```Python3 []
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # Preprocess: all positions of each value
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # Minimum distance from each position to the nearest equal value
        dist = [n] * n
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            for i, idx in enumerate(indices):
                prev_idx = indices[i - 1]
                next_idx = indices[(i + 1) % k]
                # Distance to the left: wrap around when i=0
                d_left = idx - prev_idx if i > 0 else idx + n - prev_idx
                # Distance to the right: wrap around when i=k-1
                d_right = next_idx - idx if i < k - 1 else next_idx + n - idx
                dist[idx] = min(d_left, d_right)

        # Queries
        return [dist[q] if dist[q] < n else -1 for q in queries]
```

# Complexity

| Method | Time complexity | Space complexity | Notes |
|------|-----------|-----------|------|
| Method 1: Binary search | $O(n + m \log n)$ | $O(n)$ | Each query requires binary search |
| Method 2: Two-pointer scan | $O(n + m)$ | $O(n + m)$ | Larger constant factors and extra overhead |
| Method 3: Precompute distances | $O(n + m)$ | $O(n)$ | Optimal, with the smallest constant factor |

- **Time complexity analysis**:
  - Method 1: O(n) preprocessing and O(log n) per query, for O(n + m log n) in total
  - Method 2: 2n iterations and at most 2 updates per query, for O(n + m) in total
  - Method 3: O(n) preprocessing and O(m) queries, for O(n + m) in total

- **Space complexity analysis**:
  - All three methods require O(n) space to store positions
  - Method 2 also requires O(m) space for query_map

# Code

```Python3 []
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # Preprocess: all positions of each value
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # Minimum distance from each position to the nearest equal value
        dist = [n] * n
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            for i, idx in enumerate(indices):
                prev_idx = indices[i - 1]
                next_idx = indices[(i + 1) % k]
                # Distance to the left: wrap around when i=0
                d_left = idx - prev_idx if i > 0 else idx + n - prev_idx
                # Distance to the right: wrap around when i=k-1
                d_right = next_idx - idx if i < k - 1 else next_idx + n - idx
                dist[idx] = min(d_left, d_right)

        # Queries
        return [dist[q] if dist[q] < n else -1 for q in queries]
```

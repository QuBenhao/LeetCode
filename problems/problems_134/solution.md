# [Python/Go/C] Simulation

> Author: Benhao
> Date: 2024-02-26
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [134. 加油站](https://leetcode.cn/problems/gas-station/description/)

[TOC]

# Intuition

> Simulate starting from A. If the trip cannot continue from B, starting from any point between A and B will not work either, because reaching the next point leaves a nonnegative amount of gas. Next, try starting from the point after B. Repeat until no starting points remain to try.

# Approach

> Start at 0 and simulate the remaining gas. If the trip cannot continue from a point, change the starting point to the next one. If the new start is a previously visited point, no answer exists.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        n = len(gas)
        while idx < n:
            if not gas[idx]:
                idx += 1
                continue
            cur = 0
            for i in range(idx, n + idx):
                cur += gas[i % n] - cost[i % n]
                if cur < 0:
                    if idx >= i % n + 1:
                        return -1
                    idx = i % n + 1
                    break
            else:
                return idx
        return -1
```
```Go []
func canCompleteCircuit(gas []int, cost []int) int {
    for idx, n := 0, len(gas); idx < n; {
        if gas[idx] == 0 {
            idx++
            continue
        }
        cur, ok := 0, true
        for i := idx; i < idx + n; i++ {
            cur += gas[i % n] - cost[i % n]
            if cur < 0 {
                if nxt := i % n + 1; idx >= nxt {
                    return -1
                } else {
                    idx = nxt
                }
                ok = false
                break
            }
        }
        if ok {
            return idx
        }
    }
    return -1
}
```
```C []
int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    for (int idx = 0; idx < gasSize; ) {
        if (gas[idx] == 0) {
            idx++;
            continue;
        }
        int cur = 0;
        for (int i = idx; i < idx + gasSize; i++) {
            cur += gas[i % gasSize] - cost[i % gasSize];
            if (cur < 0) {
                if (idx >= i % gasSize + 1) {
                    return -1;
                }
                idx = i % gasSize + 1;
                goto next;
            }
        }
        return idx;
        next:
    }
    return -1;
}
```
  

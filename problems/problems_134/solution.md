# [Python/Go/C] 模拟

> Author: Benhao
> Date: 2024-02-26
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [134. 加油站](https://leetcode.cn/problems/gas-station/description/)

[TOC]

# 思路

> 从A点开始模拟出发，如果走到B点走不下去了，说明从A到B之间的任何一个点出发都没用，因为一个点能走到下一个点，剩的油量是非负数。那么继续尝试从B点的下一个点出发。依次重试直到没有可以尝试的出发点。

# 解题方法

> 从0出发，模拟出发后的油量，如果到某点后不能再前进，就更新为那个点的下一个点，如果更新到了经历过的点，说明不存在答案。

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  

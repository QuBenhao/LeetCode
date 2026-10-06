# [Python/Golang] Hashing + mathematical greedy strategy

> Author: Benhao
> Date: 2024-05-14
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2244. 完成所有任务需要的最少轮数](https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/description/)

[TOC]

# Intuition

> Count with a hash table and greedily take as many groups of 3 as possible, using the standard case split by remainder modulo 3.

# Approach

> If the remainder is 1, take one fewer group of 3, leaving 4 tasks for two groups of 2. (A count of 1 is the exception; return immediately.)
If the remainder is 2, take all possible groups of 3 and then one group of 2.
If the count is divisible by 3, use only groups of 3.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnts = Counter(tasks)
        ans = 0
        for cnt in cnts.values():
            if cnt == 1:
                return -1
            match cnt % 3:
                case 1:
                    ans += (cnt - 4) // 3 + 2
                case 2:
                    ans += cnt // 3 + 1
                case _:
                    ans += cnt // 3
        return ans
```
```Golang []
func minimumRounds(tasks []int) (ans int) {
    counter := map[int]int{}
    for _, v := range tasks {
        counter[v]++
    }
    for _, v := range counter {
        if v == 1 {
            return -1
        }
        switch v % 3 {
        case 1:
            ans += (v - 4) / 3 + 2
        case 2:
            ans += (v - 2) / 3 + 1
        default:
            ans += v / 3
        }
    }
    return
}
```


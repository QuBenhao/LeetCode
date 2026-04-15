# [Python/Golang] 哈希+数学贪心

> Author: Benhao
> Date: 2024-05-14
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2244. 完成所有任务需要的最少轮数](https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/description/)

[TOC]

# 思路

> 哈希统计，贪心尽可能多地取3，经典的按3求余分类取法

# 解题方法

> 如果模3余1，少取一个3，剩出个4取两次2 （1是例外，直接返回）
如果模3余2，取所有3后再取一个2
如果整除3，就全取3

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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


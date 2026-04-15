# [Python/Go] 前缀和 or 滑动窗口

> Author: Benhao
> Date: 2024-05-05
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [1652. 拆炸弹](https://leetcode.cn/problems/defuse-the-bomb/description/)

[TOC]

# 思路

> 多个连续的和用前缀和。固定的k长度和用滑动窗口

# 复杂度

时间复杂度:
> $O(n)$


# Code
```Python3 [前缀和]
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        presum = list(itertools.accumulate(code + code))
        return [presum[i + k] - presum[i] if k > 0 else presum[n + i - 1] - presum[n + i - 1 + k] for i in range(n)]
```
```Python3 []
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        s = sum(code[1:k+1] if k > 0 else code[k:])
        for i in range(n):
            ans[i] = s
            s += code[i % n] - code[(i + k) % n] if k < 0 else code[(i + k + 1) % n] - code[(i + 1) % n]
        return ans
```
```Golang []
func sum(arr []int) (ans int) {
    for _, v := range arr {
        ans += v
    }
    return
}

func decrypt(code []int, k int) []int {
    n := len(code)
    ans := make([]int, n)
    if k == 0 {
        return ans
    }
    var s int
    if k > 0 {
        s = sum(code[1:k+1]) 
    } else {
        s = sum(code[n + k:])
    }
    for i := 0; i < n; i++ {
        ans[i] = s
        if k > 0 {
            s += code[(i + k + 1) % n] - code[(i + 1) % n]
        } else {
            s += code[i % n] - code[(i + k + n) % n]
        }
    }
    return ans
}
```

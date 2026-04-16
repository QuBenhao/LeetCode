# 数学贪心

> Author: Benhao
> Date: 2022-12-16
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1785. 构成特定和需要添加的最少元素](https://leetcode.cn/problems/minimum-elements-to-add-to-form-a-given-sum/description/)

[TOC]

# 思路
> 每次添加尽可能大或尽可能小的数来弥补差距

# 解题方法
> 向上取整可得需要多少

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(1)$

# Code
```Python3 []

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return ceil(abs((goal - sum(nums))) / abs(limit))
```
```Cpp []
#define i64 long long

class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        i64 tot = accumulate(nums.begin(), nums.end(), 0l), diff = abs(tot - goal);
        return diff / limit + (diff % limit == 0 ? 0 : 1);
    }
};
```

感谢 [@全力以赴✨](/u/endless_developy) 提供的其他语言版本

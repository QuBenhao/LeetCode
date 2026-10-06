# Mathematics and greedy

> Author: Benhao
> Date: 2022-12-16
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1785. 构成特定和需要添加的最少元素](https://leetcode.cn/problems/minimum-elements-to-add-to-form-a-given-sum/description/)

[TOC]

# Intuition
> Add the largest or smallest allowed value each time to close the gap.

# Approach
> Round up to obtain the number needed.

# Complexity
- Time complexity:
> $O(n)$

- Space complexity:
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

Thanks to [@全力以赴✨](/u/endless_developy) for the implementations in other languages.

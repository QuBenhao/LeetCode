# 从二分查找到一次遍历

> Author: Benhao
> Date: 2026-04-15
> Upvotes: 1
> Tags: Python3

---

> Problem: [3488. 距离最小相等元素查询](https://leetcode.cn/problems/closest-equal-element-queries/description/)

[TOC]

# 思路

本题提供三种解法，从易想到到最优：

1. **方法一：二分查找** - 最容易想到，预处理 + 二分
2. **方法二：双指针扫描** - 一次遍历，但常数较大
3. **方法三：预处理距离数组** - 最优解，O(n+m) 时间复杂度

# 解题过程

## 方法一：二分查找

**核心思想**：预处理每个值出现的所有位置（有序列表），对每个查询用二分找到左右最近的位置。

**具体步骤**：
1. 用字典记录每个值的所有出现位置，自然有序
2. 对于查询位置 `q`，找到 `nums[q]` 的位置列表
3. 用 `bisect_left` 找到 `q` 在列表中的位置
4. 比较左边和右边相邻位置的距离，取最小
5. 特别处理环形数组：首尾位置的距离需要加上 `n`

```Python3 []
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # 预处理：记录每个值出现的所有位置
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
            # 二分查找 q 在 positions 中的位置
            idx = bisect_left(positions, q)
            
            # 检查左边
            if idx > 0:
                min_dist = min(min_dist, q - positions[idx - 1])
            # 检查右边
            if idx < len(positions):
                min_dist = min(min_dist, positions[idx] - q)
            # 检查环形距离
            min_dist = min(min_dist, 
                          positions[0] + n - q,  # 从尾部绕
                          positions[-1] - q if positions[-1] <= q else q + n - positions[-1])
            
            ans.append(min_dist)
        
        return ans
```

## 方法二：双指针扫描

**核心思想**：遍历数组两遍（模拟环形），维护每个值最后出现的位置，更新答案。

**具体步骤**：
1. 用 `query_map` 记录每个查询位置对应的答案下标
2. 遍历 `nums + nums`（模拟环形数组）
3. 对于每个位置，更新该位置和上一个同值位置的答案
4. 最后处理未更新的答案（无同值元素）

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

**问题**：
- `nums + nums` 创建新数组，有额外开销
- `i % n` 取模运算开销大
- 嵌套循环虽然总次数是 O(m)，但常数较大

## 方法三：预处理距离数组（最优）

**核心思想**：直接预处理每个位置到最近同值元素的距离，查询时 O(1) 返回。

**具体步骤**：
1. 预处理：用字典记录每个值的所有位置
2. 对于每个值的位置列表，计算每个位置到左右相邻位置的距离
3. 特别处理环形：列表首尾需要跨数组边界计算距离
4. 查询时直接返回预处理结果

```Python3 []
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # 预处理：每个值的所有位置
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # 每个位置到最近同值的最小距离
        dist = [n] * n
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            for i, idx in enumerate(indices):
                prev_idx = indices[i - 1]
                next_idx = indices[(i + 1) % k]
                # 左边距离：i=0 时环形
                d_left = idx - prev_idx if i > 0 else idx + n - prev_idx
                # 右边距离：i=k-1 时环形
                d_right = next_idx - idx if i < k - 1 else next_idx + n - idx
                dist[idx] = min(d_left, d_right)

        # 查询
        return [dist[q] if dist[q] < n else -1 for q in queries]
```

# 复杂度

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 方法一：二分查找 | $O(n + m \log n)$ | $O(n)$ | 每次查询需要二分 |
| 方法二：双指针扫描 | $O(n + m)$ | $O(n + m)$ | 常数较大，有额外开销 |
| 方法三：预处理距离 | $O(n + m)$ | $O(n)$ | 最优解，常数最小 |

- **时间复杂度分析**：
  - 方法一：预处理 O(n)，每个查询 O(log n)，总共 O(n + m log n)
  - 方法二：遍历 2n 次，每个查询最多更新 2 次，总共 O(n + m)
  - 方法三：预处理 O(n)，查询 O(m)，总共 O(n + m)

- **空间复杂度分析**：
  - 三种方法都需要 O(n) 存储位置信息
  - 方法二额外需要 O(m) 的 query_map

# Code

```Python3 []
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # 预处理：每个值的所有位置
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # 每个位置到最近同值的最小距离
        dist = [n] * n
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            for i, idx in enumerate(indices):
                prev_idx = indices[i - 1]
                next_idx = indices[(i + 1) % k]
                # 左边距离：i=0 时环形
                d_left = idx - prev_idx if i > 0 else idx + n - prev_idx
                # 右边距离：i=k-1 时环形
                d_right = next_idx - idx if i < k - 1 else next_idx + n - idx
                dist[idx] = min(d_left, d_right)

        # 查询
        return [dist[q] if dist[q] < n else -1 for q in queries]
```

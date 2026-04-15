# 乘法差分 + 余数类分组 + 费马小定理求逆元

> Author: Benhao
> Date: 2026-04-08
> Upvotes: 1
> Tags: Python3

---

> Problem: [3655. 区间乘法查询后的异或 II](https://leetcode.cn/problems/xor-after-range-multiplication-queries-ii/description/)

[TOC]

# 思路

> 你选用何种方法解题？

**乘法差分 + 余数类分组 + 费马小定理求逆元**

核心思想：
1. **乘法差分**：类比加法差分，用乘法和逆元替代加法和减法
2. **余数类分组**：将等差序列 `l, l+k, l+2k, ...` 按步长 `k` 分成 `k` 个余数类，每个余数类内部位置连续，可应用差分
3. **费马小定理**：`MOD = 10^9+7` 是质数，用 `pow(v, MOD-2, MOD)` 求模逆元

# 解题过程

> 这些方法具体怎么运用？

## 1. 分析操作本质

每个查询 `[l, r, k, v]` 影响等差序列 `l, l+k, l+2k, ..., ≤r`，每个位置的最终值为：

```
nums[i] = 原值 × (所有覆盖该位置的 v 的乘积) mod MOD
```

## 2. 乘法差分原理

| 操作类型 | 区间操作 | 差分实现 | 还原方式 |
|---------|---------|---------|---------|
| 加法 | `[l,r]` 加 `x` | `diff[l] += x, diff[r+1] -= x` | 前缀和 |
| 乘法 | `[l,r]` 乘 `v` | `diff[l] *= v, diff[r+1] *= v⁻¹` | 前缀积 |

## 3. 费马小定理求逆元

模运算下不能直接除，需用逆元。由费马小定理 `a^(p-1) ≡ 1 (mod p)` 得：

```
a^(-1) ≡ a^(p-2) (mod p)
```

故 `v` 的逆元为 `pow(v, MOD-2, MOD)`。

## 4. 余数类分组处理

对于步长 `k`，位置按 `i % k` 分成 `k` 个余数类，每个类内位置"连续"（从该类视角），可独立应用差分。

差分边界计算：操作 `[l, r, k, v]` 影响位置 `l, l+k, ..., l+mk ≤ r`

- 起点：`l` 处乘 `v`
- 终点：`l + ((r-l)//k + 1) * k` 处乘 `v⁻¹`（若 `< n`）

## 5. 实现流程

1. 按步长 `k` 分组所有查询
2. 对每个 `k`：构建差分数组 → 按余数类分组差分点 → 计算前缀积
3. 最终计算异或结果

# 复杂度

- 时间复杂度: $O(q + \sum \text{有效覆盖范围})$，每个查询添加 $O(1)$ 个差分点，遍历时只处理有操作的位置
- 空间复杂度: $O(n + q)$，存储差分数组和结果数组

# Code
```Python3 []
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # 每个位置需要乘的总乘数
        mult = [1] * n

        # 按 k 分组处理
        groups = defaultdict(list)  # k -> [(l, r, v), ...]
        for l, r, k, v in queries:
            groups[k].append((l, r, v))

        for k, ops in groups.items():
            # 差分数组
            diff = defaultdict(lambda: 1)

            for l, r, v in ops:
                diff[l] = (diff[l] * v) % MOD
                next_pos = l + ((r - l) // k + 1) * k
                if next_pos < n:
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[next_pos] = (diff[next_pos] * inv_v) % MOD

            # 按余数类分组处理差分点
            # rem_diffs[rem] = [(pos, val), ...]
            rem_diffs = defaultdict(list)
            for pos, val in diff.items():
                rem_diffs[pos % k].append((pos, val))

            for rem, items in rem_diffs.items():
                items.sort()
                cur = 1
                idx = 0
                for pos in range(rem, n, k):
                    # 应用该位置的所有差分
                    while idx < len(items) and items[idx][0] == pos:
                        cur = (cur * items[idx][1]) % MOD
                        idx += 1
                    mult[pos] = (mult[pos] * cur) % MOD

        # 最终结果
        result = 0
        for i in range(n):
            val = (nums[i] * mult[i]) % MOD
            result ^= val
        return result
```

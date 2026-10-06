# Multiplicative differences + grouping by residue class + modular inverses using Fermat's little theorem

> Author: Benhao
> Date: 2026-04-08
> Upvotes: 1
> Tags: Python3

---

> Problem: [3655. 区间乘法查询后的异或 II](https://leetcode.cn/problems/xor-after-range-multiplication-queries-ii/description/)

[TOC]

# Intuition

> Which approach do you use to solve the problem?

**Multiplicative differences + grouping by residue class + modular inverses using Fermat's little theorem**

Core idea:
1. **Multiplicative differences**: Analogous to additive differences, using multiplication and inverses in place of addition and subtraction
2. **Grouping by residue class**: For step size `k`, divide positions into `k` residue classes; the arithmetic progression `l, l+k, l+2k, ...` is consecutive within its class, so differences apply
3. **Fermat's little theorem**: `MOD = 10^9+7` is prime; use `pow(v, MOD-2, MOD)` to find the modular inverse

# Solution steps

> How are these methods applied?

## 1. Understand the operation

Each query `[l, r, k, v]` affects the arithmetic progression `l, l+k, l+2k, ..., ≤r`. The final value at each position is:

```
nums[i] = original value × (product of all v values covering this position) mod MOD
```

## 2. Multiplicative differences

| Operation type | Range operation | Difference update | Reconstruction |
|---------|---------|---------|---------|
| Addition | Add `x` to `[l,r]` | `diff[l] += x, diff[r+1] -= x` | Prefix sums |
| Multiplication | Multiply `[l,r]` by `v` | `diff[l] *= v, diff[r+1] *= v⁻¹` | Prefix products |

## 3. Modular inverses using Fermat's little theorem

Division cannot be used directly in modular arithmetic; use an inverse instead. Fermat's little theorem, `a^(p-1) ≡ 1 (mod p)`, gives:

```
a^(-1) ≡ a^(p-2) (mod p)
```

Thus the inverse of `v` is `pow(v, MOD-2, MOD)`.

## 4. Process groups by residue class

For step size `k`, divide positions into `k` residue classes by `i % k`. Positions are "consecutive" within each class, so differences can be applied independently.

Calculate difference boundaries: operation `[l, r, k, v]` affects positions `l, l+k, ..., l+mk ≤ r`

- Start: multiply by `v` at `l`
- End: multiply by `v⁻¹` at `l + ((r-l)//k + 1) * k` (if `< n`)

## 5. Implementation steps

1. Group all queries by step size `k`
2. For each `k`: build a difference array → group difference points by residue class → compute prefix products
3. Finally, compute the XOR result

# Complexity

- Time complexity: $O(q + \sum \text{effective covered range})$. Each query adds $O(1)$ difference points, and traversal processes only positions affected by operations
- Space complexity: $O(n + q)$, for the difference array and result array

# Code
```Python3 []
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # Total multiplier for each position
        mult = [1] * n

        # Process groups by k
        groups = defaultdict(list)  # k -> [(l, r, v), ...]
        for l, r, k, v in queries:
            groups[k].append((l, r, v))

        for k, ops in groups.items():
            # Difference array
            diff = defaultdict(lambda: 1)

            for l, r, v in ops:
                diff[l] = (diff[l] * v) % MOD
                next_pos = l + ((r - l) // k + 1) * k
                if next_pos < n:
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[next_pos] = (diff[next_pos] * inv_v) % MOD

            # Process difference points grouped by residue class
            # rem_diffs[rem] = [(pos, val), ...]
            rem_diffs = defaultdict(list)
            for pos, val in diff.items():
                rem_diffs[pos % k].append((pos, val))

            for rem, items in rem_diffs.items():
                items.sort()
                cur = 1
                idx = 0
                for pos in range(rem, n, k):
                    # Apply all differences at this position
                    while idx < len(items) and items[idx][0] == pos:
                        cur = (cur * items[idx][1]) % MOD
                        idx += 1
                    mult[pos] = (mult[pos] * cur) % MOD

        # Final result
        result = 0
        for i in range(n):
            val = (nums[i] * mult[i]) % MOD
            result ^= val
        return result
```

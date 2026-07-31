> Author: Benhao
> Date: 2026-08-01
> Tags: Python3

---

> Problem: [486. 预测赢家](https://leetcode.cn/problems/predict-the-winner/description/)

[TOC]

# 思路

1. 这是一道两人零和博弈题，玩家 1 先手、双方都采取最优策略，问玩家 1 的总分能否不低于玩家 2（平局也算赢）。
2. 核心状态设计为「当前区间 `[l, r]` 在双方最优博弈下，玩家 1 与玩家 2 的得分差」`diff`。由于零和，得分差最大即玩家 1 最优、最小即玩家 2 最优，于是同一套 minimax 即可覆盖两人。
3. 用符号 `sig` 区分当前轮到谁：`sig = 1` 表示玩家 1（最大化差值，取走的数字按 `+nums` 计入）；`sig = -1` 表示玩家 2（最小化差值，取走的数字按 `-nums` 计入，等价于玩家 1 相对落后）。
4. 当前是谁的回合只取决于「已取走了几个数」：已取 `n - (r - l + 1)` 个。取走偶数个 → 轮到玩家 1，否则玩家 2。用区间长度与总长的奇偶是否相同即可判定，写成 `sig = -1 if (r - l + 1) & 1 != n & 1 else 1`。

# 解题过程

> 区间记忆化搜索（minimax）

- 定义 `dfs(l, r)`：返回区间 `[l, r]` 在双方最优下的得分差。
- 边界：只剩一个数 `l == r`，当前玩家独吞它，返回 `nums[l] * sig`。
- 转移：当前玩家可拿左端或右端。拿左端后剩余 `[l+1, r]`，得分差变为 `dfs(l+1, r) + sig * nums[l]`；拿右端同理 `dfs(l, r-1) + sig * nums[r]`。
- 玩家 1 回合（`sig > 0`）取两者较大值，玩家 2 回合（`sig < 0`）取两者较小值。
- 最终判断 `dfs(0, n-1) >= 0` 即可。`@cache` 记忆化避免重复计算。

# 极小化极大算法（Minimax）

这是零和博弈中双方都采取最优策略时的通用决策框架。博弈可画成一棵「游戏树」：每个结点是一个局面，边是某一方的一步走法；叶子结点给出终局收益。

- 轮到 **MAX 方** 时，它想让自己收益最大，于是从子结点里取最大值：`value = max(value(child))`。
- 轮到 **MIN 方** 时，它想压低 MAX 的收益（零和即等于让自己收益最大），于是取最小值：`value = min(value(child))`。
- 两方沿树交替 max / min，逐层回溯到根，根的值就是「在双方都最优时 MAX 能获得的最终收益」。本题要的正是这个值是否 ≥ 0。

通常会写成两个互相调用的函数 `maxValue` / `minValue`，或显式传一个 `turn` 参数区分当前是谁。本解法的 `sig` 写法正是它的等价简化：

- 因为零和，双方其实共用同一个「玩家 1 − 玩家 2 得分差」状态，只是目标相反。把「当前是谁的回合」编码成一个符号 `sig`：
  - `sig = 1`（轮到玩家 1，MAX 方）：差值按 `+nums` 计入，并在子状态里取 **max**；
  - `sig = -1`（轮到玩家 2，MIN 方）：差值按 `-nums` 计入（玩家 2 拿走即玩家 1 相对落后），并在子状态里取 **min**。
- 于是两个交替的 `max` / `min` 被合并成「同一个递归 + 一个带符号的取极函数」，`sig` 同时承载了「收益符号」和「取大还是取小」两件事。这就是代码里 `sig` 写法与标准 Minimax 的对应关系。

补充：Minimax 在状态爆炸时常用 **α–β 剪枝** 提前砍掉不可能被选择的子树来提速；本题状态只有 $O(n^2)$ 且都需展开，故不剪枝，直接记忆化即可。

# 复杂度

- 时间复杂度: $O(n^2)$ —— 状态 `(l, r)` 共 $O(n^2)$ 个，每状态 $O(1)$ 计算。
- 空间复杂度: $O(n^2)$ —— 缓存表大小 $O(n^2)$，递归栈深度 $O(n)$。

# Code
```Python3 []
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def minmax(l, r):
            sig = -1 if (r - l + 1) & 1 != n & 1 else 1
            if l == r:
                return nums[l] * sig
            ans = minmax(l + 1, r) + sig * nums[l]
            if sig < 0:
                sig = min(ans, minmax(l, r - 1) + sig * nums[r])
            else:
                sig = max(ans, minmax(l, r - 1) + sig * nums[r])
            return sig

        return minmax(0, n - 1) >= 0
```

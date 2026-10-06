> Author: Benhao
> Date: 2026-08-01
> Tags: Python3

---

> Problem: [486. 预测赢家](https://leetcode.cn/problems/predict-the-winner/description/)

[TOC]

# Intuition

1. This is a two-player zero-sum game. Player 1 moves first, both play optimally, and the question is whether player 1 can score at least as much as player 2. A tie counts as a win.
2. Define the state `diff` as the score difference between player 1 and player 2 for the current interval `[l, r]` under optimal play. In a zero-sum game, player 1 maximizes this difference and player 2 minimizes it, so one minimax formulation covers both players.
3. Use `sig` to distinguish turns: `sig = 1` for player 1, who maximizes the difference and contributes `+nums`; `sig = -1` for player 2, who minimizes the difference and contributes `-nums`, reducing player 1's relative score.
4. The turn depends only on how many numbers have been taken: `n - (r - l + 1)`. An even count means player 1's turn; otherwise, player 2's. Compare the parity of the interval length and total length: `sig = -1 if (r - l + 1) & 1 != n & 1 else 1`.

# Solution steps

> Memoized interval search (minimax)

- Define `dfs(l, r)` to return the score difference for interval `[l, r]` under optimal play.
- Base case: When only one number remains, `l == r`, the current player takes it; return `nums[l] * sig`.
- Transition: Take either endpoint. Taking the left leaves `[l+1, r]` and gives `dfs(l+1, r) + sig * nums[l]`; taking the right similarly gives `dfs(l, r-1) + sig * nums[r]`.
- On player 1's turn (`sig > 0`), choose the larger result; on player 2's turn (`sig < 0`), choose the smaller.
- Finally, check `dfs(0, n-1) >= 0`. Memoization with `@cache` avoids repeated computation.

# Minimax

Minimax is a general decision framework for zero-sum games in which both players act optimally. A game tree represents each position as a node and each move as an edge; leaves give the final payoff.

- On **MAX's** turn, choose the child with the greatest payoff: `value = max(value(child))`.
- On **MIN's** turn, minimize MAX's payoff, which maximizes MIN's payoff in a zero-sum game: `value = min(value(child))`.
- Alternate max / min while propagating values back to the root. The root value is MAX's final payoff under optimal play. This problem asks whether that value is ≥ 0.

Typical implementations use mutually recursive `maxValue` / `minValue` functions or an explicit `turn` parameter. The `sig` approach here is an equivalent simplification:

- Both players share the same state, the score difference player 1 − player 2, but have opposite objectives. Encode the current turn as `sig`:
  - `sig = 1` (player 1, MAX): contribute `+nums` to the difference and take the **max** of child states.
  - `sig = -1` (player 2, MIN): contribute `-nums`, since player 2's gain reduces player 1's relative score, and take the **min**.
- The alternating `max` / `min` functions become one recursive function with a signed extremum operation. `sig` controls both the payoff sign and whether to maximize or minimize, matching standard Minimax.

Note: Minimax often uses **α–β pruning** to skip subtrees that cannot affect the decision when the state space grows large. Here there are only $O(n^2)$ states, all requiring evaluation, so memoization suffices without pruning.

# Complexity

- Time complexity: $O(n^2)$ — there are $O(n^2)$ states `(l, r)`, each requiring $O(1)$ work.
- Space complexity: $O(n^2)$ — the cache has $O(n^2)$ entries and the recursion depth is $O(n)$.

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

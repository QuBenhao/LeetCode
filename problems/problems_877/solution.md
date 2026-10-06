# [Python] Greedy

> Author: Benhao
> Date: 2021-06-15
> Upvotes: 15
> Tags: Python, Python3

---

After thinking it through, I cannot see how the second player can win: the first player can also obtain any winning selection available to the second.

Disaster: after changing the network adapter, I cannot post.

- The length is even and the sum is odd:
    - Both players take the same number of piles
    - Their totals differ regardless of how they choose

- On every first-player turn, the array length is even, and the endpoints' original indices have different parity.
- On every second-player turn, the array length is odd, and the endpoints' original indices have the same parity.

The first player can choose `odd or even positions` and force the second player to take only `even or odd positions`, respectively.
Either the `sum at odd positions` or the `sum at even positions` must be larger. The first player can always take the larger sum and therefore always wins.

```python3
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
```

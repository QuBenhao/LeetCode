# [Python] Proof by contradiction: the first player wins with an even count

> Author: Benhao
> Date: 2021-05-22
> Upvotes: 1
> Tags: Python, Python3

---

## Approach
**When nums has even length, the first player always wins**
> `Proof by contradiction: assume Bob always wins regardless of which number Alice erases`
> Since the array has even length, Bob cannot win by having all numbers erased: Bob must make the last erasure after an even number of turns. There must therefore be a turn on which every number Alice could erase leaves an XOR of 0
> That is, `n1 ^ n2 ^ ... nk = a` (a!=0), `n1 ^ n2 ^..^ nk-1` = `n2 ^..^ nk` = `n1 ^ n3 ^.. ^ nk` = 0
> All the expressions above hold if and only if `n1 = n2 = .. = nk = a` and `k is odd`
> This means an odd number of copies of a remain, so the array has odd length on Alice's turn, contradicting the even length of nums
        
**If nums has odd length, Alice can win only if the XOR of nums is already 0**
Whatever number Alice erases, the array becomes even in length with Bob to move, so Bob is guaranteed to win

## Code
```python3
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 or reduce(xor,nums) == 0
```

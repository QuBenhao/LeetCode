# [Python/Java] Game theory

> slug: pythonjava-bo-yi-lun-by-himymben-ybrs
> date: 2021-09-17
> tags: Java, Python, Python3
> question: Nim Game (nim-game)
> url: https://leetcode.cn/problems/nim-game/solutions/gK224m/pythonjava-bo-yi-lun-by-himymben-ybrs/

---
### Approach
Each player can take 1-3 stones, so the second player can always take the complement to 4 of the first player's move (for example, taking 3 when the opponent takes 1). Each pair of turns then removes exactly 4 stones. Thus, if the number of stones is a multiple of 4, the second player can always take the last stone.

If the number of stones is not a multiple of 4, its remainder modulo 4 is 1-3. The first player can take that remainder, becoming the effective second player in the strategy above and guaranteeing a win.

> Aside: This resembles the childhood game of counting to 21. Each player says one to three consecutive numbers, starting at 1, and whoever says 21 wins. To win as the first player, avoid saying 18, since the opponent could then reach 21. To avoid 18, avoid 14, since the opponent could reach 17 and force you to say 18. Continuing backward, the number to avoid is 2. Therefore, start by saying only 1, and you can force a win.

### Code

```Python3 []
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```
```Java []
class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}
```

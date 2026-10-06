# [Python/Java/TypeScript/Go] Brain teaser

> slug: pythonjavatypescriptgo-by-himymben-glmm
> date: 2022-07-07
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Minimum Cost to Move Chips to The Same Position (minimum-cost-to-move-chips-to-the-same-position)
> url: https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/solutions/riIT9L/pythonjavatypescriptgo-by-himymben-glmm/

---
### Approach
Moving a chip by 2 costs nothing, so all chips can be moved to positions [1, 2] at no cost.
The problem reduces to choosing the position in [1, 2] with fewer chips. That count is the answer: no sequence of moves can avoid paying at least this much.
In other words, take the smaller of the counts of odd and even positions.

### Code

```Python3 []
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(odds := sum(p & 1 for p in position), len(position) - odds)
```
```Java []
class Solution {
    public int minCostToMoveChips(int[] position) {
        int odds = 0;
        for (int p: position) {
            odds += p & 1;
        }
        return Math.min(odds, position.length - odds);
    }
}
```
```TypeScript []
function minCostToMoveChips(position: number[]): number {
    let odds = 0
    for (const p of position) {
        odds += p & 1
    }
    return Math.min(odds, position.length - odds)
};
```
```Go []
func minCostToMoveChips(position []int) int {
    odds := 0
    for _, p := range position {
        odds += p & 1
    }
    if evens := len(position) - odds; odds < evens {
        return odds
    } else {
        return evens
    }
}
```

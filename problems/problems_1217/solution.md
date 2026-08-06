# [Python/Java/TypeScript/Go] 脑筋急转弯

> slug: pythonjavatypescriptgo-by-himymben-glmm
> date: 2022-07-07
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Minimum Cost to Move Chips to The Same Position (minimum-cost-to-move-chips-to-the-same-position)
> url: https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/solutions/riIT9L/pythonjavatypescriptgo-by-himymben-glmm/

---
### 解题思路
题目中筹码移动2个距离是不花费任何代价的，所有筹码都可以被移到[1, 2]中 (不费任何代价)。
题目变为比较[1, 2]中哪个筹码更少 (这个代价是不可能被省略的，不管怎么挪动都至少需要这么多)，即为答案。
也就是数据中奇数少还是偶数少。

### 代码

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
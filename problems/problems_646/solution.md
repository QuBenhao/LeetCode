# [Python/Java/TypeScript/Go] Sorting + greedy

> Author: Benhao
> Date: 2022-09-03
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Suppose two intervals overlap: [$a_1$, $b_1$] and [$a_2$, $b_2$]. Without loss of generality, let $a_2 \le b_1 \le b_2$.
Choosing the first is better because its endpoint lies farther left, leaving room for more intervals.
Sort by right endpoint, then traverse while tracking the right endpoint of the last selected interval.
If a later interval starts before the current right endpoint, it overlaps. Its right endpoint is farther right, so it is no better than the interval already selected.
Count how many intervals can be selected using this rule.

### Code

```Python3 []
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans, cur = 0, -inf
        for l, r in pairs:
            if cur < l:
                ans += 1
                cur = r
        return ans
```
```Java []
class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b)-> a[1] - b[1]);
        int ans = 0, cur = Integer.MIN_VALUE;
        for (int[] pair: pairs) {
            if (cur < pair[0]) {
                cur = pair[1];
                ans++;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function findLongestChain(pairs: number[][]): number {
    pairs.sort((a, b)=>a[1]-b[1])
    let ans: number = 0, cur: number = Number.MIN_SAFE_INTEGER
    for (const [left, right] of pairs) {
        if (cur < left) {
            cur = right
            ans++
        }
    }
    return ans
};
```
```Go []
const INT_MAX = int(^uint(0) >> 1)
const INT_MIN = ^INT_MAX

func findLongestChain(pairs [][]int) (ans int) {
    sort.Slice(pairs, func(i, j int) bool { return pairs[i][1] < pairs[j][1] })
    cur := INT_MIN
    for _, pair := range pairs {
        if cur < pair[0] {
            cur = pair[1]
            ans++
        }
    }
    return
}
```

# [Python/Java/TypeScript/Go] 排序 + 贪心

> Author: Benhao
> Date: 2022-09-03
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
假设存在两个重叠区间, [$a_1$, $b_1$] 和 [$a_2$, $b_2$], 不妨设$a_2 \le b_1 \le b_2$,
这个时候取前者是比取后者更优的，因为这样"前进"的边界最靠左，可以更多地加入其他区间。
我们按右端点排序，遍历时维护一个当前覆盖到的区间右端点，
如果后面的左端点在当前右端点之前，说明有重叠且因为后面的右端点在当前右端点的右边，是不如当前右端点更优的。
按照这种选择统计有多少区间可以被取即可。

### 代码

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
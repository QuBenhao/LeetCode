# [Python/Java/JavaScript/Go] Applying prefix sums

> slug: pythonjavajavascriptgo-qian-zhui-he-ying-26nk
> date: 2022-03-07
> tags: Go, Java, JavaScript, Python, Python3
> question: Plates Between Candles (plates-between-candles)
> url: https://leetcode.cn/problems/plates-between-candles/solutions/culeny/pythonjavajavascriptgo-qian-zhui-he-ying-26nk/

---
### Approach
For each range query, we need the following information:
1. The first candle at or to the right of the left endpoint.
2. The first candle at or to the left of the right endpoint.
3. The number of plates between these two candles.

Finding the nearest candle on each side of every position is a simple dynamic-programming problem.
Counting items of a given type between two positions is a standard use of prefix sums.


### Code

```Python3 []
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # presum: prefix counts of *; lefts: nearest | at or to the left of each position; rights: nearest | at or to the right
        presum, lefts, rights, l = [0] * (n + 1), [-1] * n, [-1] * n, -1
        for i, c in enumerate(s):
            if c == '*':
                # The current character is *, so increment the prefix count
                presum[i + 1] = presum[i] + 1
            else:
                # The current character is |, so the prefix count stays the same
                presum[i + 1] = presum[i]
                # Update the nearest candle position (it remains i until the next update)
                l = i
            lefts[i] = l
        # Compute right-side positions the same way, scanning from right to left
        r = -1
        for i, c in enumerate(s[::-1]):
            if c == '|':
                r = n - 1 - i
            rights[n - 1 - i] = r
        # Plates can exist only if both boundary candles exist and the right candle lies to the right of the left candle; otherwise the answer is 0
        return [presum[lefts[r]] - presum[rights[l]] if rights[l] >= 0 and lefts[r] >= 0 and rights[l] < lefts[r] else 0 for l, r in queries]
```
```Java []
class Solution {
    public int[] platesBetweenCandles(String s, int[][] queries) {
        int n = s.length();
        int[] presum = new int[n + 1], lefts = new int[n], rights = new int[n];
        for(int i = 0, j = n - 1, l = -1, r = -1; i < n; i++, j--) {
            if(s.charAt(i) == '*')
                presum[i + 1] = presum[i] + 1;
            else {
                presum[i + 1] = presum[i];
                l = i;
            }
            if(s.charAt(j) == '|')
                r = j;
            lefts[i] = l;
            rights[j] = r;
        }
        int[] ans = new int[queries.length];
        for(int i = 0; i < queries.length; i++)
            if(lefts[queries[i][1]] >= 0 && rights[queries[i][0]] >= 0 && lefts[queries[i][1]] > rights[queries[i][0]])
                ans[i] = presum[lefts[queries[i][1]]] - presum[rights[queries[i][0]] + 1];
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var platesBetweenCandles = function(s, queries) {
    const n = s.length
    const presum = new Array(n + 1).fill(0), lefts = new Array(n), rights = new Array(n)
    for(let i = 0, j = n - 1, l = -1, r = -1; i < n; i++, j--) {
        if(s.charAt(i) == '*')
            presum[i + 1] = presum[i] + 1
        else {
            presum[i + 1] = presum[i]
            l = i
        }
        if(s.charAt(j) == '|')
            r = j
        lefts[i] = l
        rights[j] = r
    }
    ans = new Array(queries.length).fill(0)
    for(let i = 0; i < queries.length; i++)
        if(lefts[queries[i][1]] >= 0 && rights[queries[i][0]] >= 0 && lefts[queries[i][1]] > rights[queries[i][0]])
            ans[i] = presum[lefts[queries[i][1]]] - presum[rights[queries[i][0]]]
    return ans
};
```
```Go []
func platesBetweenCandles(s string, queries [][]int) []int {
    n := len(s)
    presum, lefts, rights := make([]int, n + 1), make([]int, n), make([]int, n)
    for i, j, l, r := 0, n - 1, -1, -1; i < n; i++{
        if s[i] == '*' {
            presum[i + 1] = presum[i] + 1
        } else {
            presum[i + 1] = presum[i]
            l = i
        }
        if s[j] == '|' {
            r = j
        }
        lefts[i] = l
        rights[j] = r
        j--
    }
    ans := make([]int, len(queries))
    for i := 0; i < len(queries); i++ {
        if rights[queries[i][0]] >= 0 && lefts[queries[i][1]] >= 0 && lefts[queries[i][1]] > rights[queries[i][0]] {
            ans[i] = presum[lefts[queries[i][1]]] - presum[rights[queries[i][0]]]
        }
    }
    return ans
}
```

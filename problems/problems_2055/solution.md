# [Python/Java/JavaScript/Go] 前缀和应用题

> slug: pythonjavajavascriptgo-qian-zhui-he-ying-26nk
> date: 2022-03-07
> tags: Go, Java, JavaScript, Python, Python3
> question: Plates Between Candles (plates-between-candles)
> url: https://leetcode.cn/problems/plates-between-candles/solutions/culeny/pythonjavajavascriptgo-qian-zhui-he-ying-26nk/

---
### 解题思路
对于每个区间的查询，我们关心的是以下信息:
1. 左边端点右边第一个蜡烛的位置
2. 右边端点左边第一个蜡烛的位置
3. 这两个蜡烛之间有多少盘子

统计每个点左边最近和右边最近的蜡烛是一类简单的动态规划。
而求两点之间某个类型的数量，是标准的前缀和应用。


### 代码

```Python3 []
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # presum: 统计*的前缀和, lefts: 统计每个坐标左边最近的|的坐标, rights: 统计每个坐标右边最近的|的坐标
        presum, lefts, rights, l = [0] * (n + 1), [-1] * n, [-1] * n, -1
        for i, c in enumerate(s):
            if c == '*':
                # 当前字符为*，前缀和个数加一
                presum[i + 1] = presum[i] + 1
            else:
                # 当前字符为|，前缀和个数不变
                presum[i + 1] = presum[i]
                # 更新最新的坐标最近坐标（接下来下次更新前最近的都是i）
                l = i
            lefts[i] = l
        # 右边与左边的更新同理，只需要从右往左
        r = -1
        for i, c in enumerate(s[::-1]):
            if c == '|':
                r = n - 1 - i
            rights[n - 1 - i] = r
        # 最终答案只有 左查询点的右边有蜡烛、右查询点的左边有蜡烛、且右边的蜡烛在左边的蜡烛右边中间才可能有*，否则肯定是0个
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
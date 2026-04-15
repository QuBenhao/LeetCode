# [Python/Java/JavaScript/Go] DFS

> Author: Benhao
> Date: 2022-04-17
> Upvotes: 34
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
本题和[440. 字典序的第K小数字](https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/solution/pythonjavajavascriptgo-di-gui-by-himymbe-5mq5/)大同小异。

使用前缀树 + DFS （Python要求空间O(1)可以使用yield）

### 代码

```Python3 []
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(x):
            yield x
            for nxt in range(x * 10, min(n + 1, (x + 1) * 10)):
                yield from dfs(nxt)

        return [v for i in range(1, min(n + 1, 10)) for v in dfs(i)]
```
```Java []
class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ans = new ArrayList<>();
        int cur = 1;
        for(int i = 0; i < n; i++) {
            ans.add(cur);
            if(cur * 10 <= n)
                cur *= 10;
            else {
                // 枚举到当前前缀的最深处了，需要回到上一层并到下一个同层节点
                while(cur % 10 == 9 || cur >= n)
                    cur /= 10;
                cur++;
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    const ans = new Array()
    let cur = 1
    for(let i = 0; i < n; i++) {
        ans.push(cur)
        if(cur * 10 <= n)
            cur *= 10
        else {
            while(cur % 10 == 9 || cur >= n)
                cur = Math.floor(cur / 10)
            cur++
        }
    }
    return ans
};
```
```Go []
func lexicalOrder(n int) (ans []int) {
    for i, cur := 0, 1; i < n; i++ {
        ans = append(ans, cur)
        if cur * 10 <= n {
            cur *= 10
        } else {
            for cur % 10 == 9 || cur >=n {
                cur /= 10
            }
            cur++
        }
    }
    return ans
}
```
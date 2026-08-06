# [Python/Java/JavaScript/Go] 递归

> slug: pythonjavajavascriptgo-di-gui-by-himymbe-62km
> date: 2022-01-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Gray Code (gray-code)
> url: https://leetcode.cn/problems/gray-code/solutions/PdsYHB/pythonjavajavascriptgo-di-gui-by-himymbe-62km/

---
### 解题思路
利用对称性，假设我们知道$n-1$的构造，那么我们将这个构造反转并拼在后面，在这个反转里每个数的二进制第一位补上1，就得到了$n$的构造。
- $n-1$的构造本身不管是正序还是倒序，相邻之间都是差1，而在反转中所有数都在第一位加了一个1，差异不变。
- 反转后，原先最后一位会和自己相邻，加了一个1以后，差异正好是一位。
- 反转后，原先第一位会成为最后一位，后第一位首尾相邻，加了一个1以后，差异正好是一位。

### 代码

```Python3 []
class Solution:
    @lru_cache(None)
    def grayCode(self, n: int) -> List[int]:
        return [0, 1] if n == 1 else (ans:=self.grayCode(n-1)) + [i + (1<<(n-1)) for i in ans[::-1]]
```
```Java []
class Solution {
    public List<Integer> grayCode(int n) {
        if(n == 1)
            return new ArrayList<Integer>(){{add(0);add(1);}};
        List<Integer> res = grayCode(n - 1);
        int add = 1 << (n - 1);
        for(int i=res.size()-1;i>=0;i--)
            res.add(res.get(i) + add);
        return res;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    if(n == 1)
        return [0, 1]
    const res = grayCode(n - 1), add = 1 << (n - 1)
    for(let i=res.length-1;i>=0;i--)
        res.push(res[i] + add)
    return res
};
```
```Go []
func grayCode(n int) []int {
    if n == 1 {
        return []int{0, 1}
    }
    res, add := grayCode(n-1), 1<<(n-1)
    for i := len(res) - 1;i>=0;i--{
        res = append(res, res[i] + add)
    }
    return res
}
```
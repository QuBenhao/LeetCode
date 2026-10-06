# [Python/Java/JavaScript/Go] Recursion

> slug: pythonjavajavascriptgo-di-gui-by-himymbe-62km
> date: 2022-01-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Gray Code (gray-code)
> url: https://leetcode.cn/problems/gray-code/solutions/PdsYHB/pythonjavajavascriptgo-di-gui-by-himymbe-62km/

---
### Approach
Use symmetry: given the construction for $n-1$, reverse it and append it, adding a leading 1 to each binary number in the reversed part. This gives the construction for $n$.
- In the construction for $n-1$, adjacent values differ by one bit in either forward or reverse order. Adding a leading 1 to every number in the reversed part preserves that difference.
- After reversal, the original last value is adjacent to its own copy. Adding a leading 1 makes them differ by exactly one bit.
- After reversal, the original first value becomes the last value, adjacent to the first across the ends of the sequence. Adding a leading 1 makes them differ by exactly one bit.

### Code

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

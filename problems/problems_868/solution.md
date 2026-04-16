# [Python/Java/JavaScript/Go] 位运算模拟

> Author: Benhao
> Date: 2022-04-23
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
运用lowbit求数的二进制最低位

### 代码

```Python3 []
idx_map = {1<<i:i for i in range(30)}
class Solution:
    def binaryGap(self, n: int) -> int:
        def lowbit(x):
            return x & (-x)
        
        last, ans = inf, 0
        while n:
            n -= (cur := lowbit(n))
            ans, last = max(ans, idx_map[cur] - last), idx_map[cur]
        return ans
```
```Java []
class Solution {
    private static final Map<Integer, Integer> IDX_MAP = new HashMap<>(30);
    static {
        for(int i = 0; i < 30; i++)
            IDX_MAP.put(1 << i, i);
    }
    public int binaryGap(int n) {
        int last = 30, ans = 0;
        while(n > 0) {
            int cur = lowbit(n);
            int i = IDX_MAP.get(cur);
            ans = Math.max(ans, i - last);
            last = i;
            n -= cur;
        }
        return ans;
    }

    private int lowbit(int x) {
        return x & (-x);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    let last = 30, ans = 0, i = 0
    while(n > 0) {
        if(n & 1) {
            ans = Math.max(ans, i - last)
            last = i
        }
        n >>= 1
        i += 1
    }
    return ans
};
```
```Go []
func binaryGap(n int) (ans int) {
    last := 30
    for i := 0; n > 0; i++ {
        if n & 1 > 0 {
            if v := i - last; v > ans {
                ans = v
            }
            last = i
        }
        n >>= 1
    }
    return
}
```
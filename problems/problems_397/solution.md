# [Python/Java/JavaScript/Go] 记忆化递归 - 偶数必除2 奇数两者中取最小

> slug: pythonjavajavascriptgo-ou-shu-bi-chu-2-q-rw6q
> date: 2021-11-18
> tags: Go, Java, JavaScript, Python, Python3
> question: Integer Replacement (integer-replacement)
> url: https://leetcode.cn/problems/integer-replacement/solutions/QIZGry/pythonjavajavascriptgo-ou-shu-bi-chu-2-q-rw6q/

---
### 解题思路
偶数除2永远是最优的，因为如果你要在移动两次后再除2，完全可以由除2再移动一次替代，这样操作会少一个。
也就是越在数字小的时候做加减，影响的越大，越能省操作。

奇数其实也能分类，
$4*n+1$要么加一要么减一，除二以后变为$2*n$或$2*n+1$，再运算以后变为$n$或$n+1$
既然总要变成$n$或$n+1$, 减一运算到$n$需要`3`步，而加一运算到$n$需要`4`步；减一运算到$n+1$需要`4`步，而加一运算到$n+1$同样需要`4`步；
也就是说$4*n+1$的时候减一，一定能构造出答案，比加一好或者和加一的效果一样。

同理$4*n+3$的时候加一，也一定比减一好 (除了3，3两次就到1了，加一再除再减反而会浪费步数)。

### 代码

```Python3 []
class Solution:
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        return 0 if n == 1 else (self.integerReplacement(n//2) + 1 if not n % 2 else min(self.integerReplacement(n-1), self.integerReplacement(n+1))+1)
```
```Java []
class Solution {
    private static final Map<Integer, Integer> cache = new HashMap<>(){{put(1, 0);}};
    public int integerReplacement(int n) {
        if(cache.containsKey(n))
            return cache.get(n);
        int ans;
        if(n % 2 == 0)
            ans = 1 + integerReplacement(n / 2);
        else
            // 改用等价的默认除二计算结果简化两步，避免 2^31 - 1 加一的溢出
            ans = Math.min(integerReplacement(n/2 + 1), integerReplacement(n/2)) + 2;
        cache.put(n, ans);
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
const cache = new Map();
cache.set(1, 0);
var integerReplacement = function(n) {
    if(cache.has(n))
        return cache.get(n);
    let ans;
    if(n % 2 == 0)
        ans = integerReplacement(n / 2) + 1;
    else
        ans = Math.min(integerReplacement((n-1)/2),integerReplacement(Math.floor(n/2) + 1)) + 2;
    cache.set(n, ans);
    return ans;
};
```
```Go []
var cache map[int]int

func dfs(n int) int{
    if(n == 1){
        return 0
    }
    v := cache[n]
    if v > 0 {
        return v
    }
    ans := 0
    if n % 2 == 0 {
        ans = dfs(n / 2) + 1
    } else {
        ans = min(dfs(n / 2), dfs(n / 2 + 1)) + 2
    }
    cache[n] = ans
    return ans
}

func integerReplacement(n int) int {
    cache = map[int]int{}
    return dfs(n)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

既然奇数的情况可以完全确认加一还是减一，就不需要再去min了
```Go []
func integerReplacement(n int) int {
    ans := 0
    for n > 1 {
        if n & 1 == 0 {
            n >>= 1
            ans++
        }else {
            if n % 4 == 1 {
                n >>= 2
                ans += 3
            } else {
                if n == 3 {
                    n -= 1
                    ans++
                } else {
                    n >>= 2
                    n += 1
                    ans += 3
                }
            }
        }
    }
    return ans
}
```
```Go []
func integerReplacement(n int) int {
    ans := 0
    for n > 1 {
        switch n % 4 {
            case 1:
                n >>= 2
                ans += 3
            case 3:
                if n > 3{
                    n >>= 2
                    n += 1
                    ans += 3
                } else{
                    n -= 1
                    ans++
                }
            default:
                n >>= 1
                ans++
        }
    }
    return ans
}
```
```Python3 []
class Solution:
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        return 0 if n == 1 else (self.integerReplacement(n//2) + 1 if not n % 2 else (self.integerReplacement(n//2) if n % 4 == 1 else (self.integerReplacement(n//2+1) if n > 3 else 0))+2)
```
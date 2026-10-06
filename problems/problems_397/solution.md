# [Python/Java/JavaScript/Go] Memoized recursion: halve even values and take the better choice for odd values

> slug: pythonjavajavascriptgo-ou-shu-bi-chu-2-q-rw6q
> date: 2021-11-18
> tags: Go, Java, JavaScript, Python, Python3
> question: Integer Replacement (integer-replacement)
> url: https://leetcode.cn/problems/integer-replacement/solutions/QIZGry/pythonjavajavascriptgo-ou-shu-bi-chu-2-q-rw6q/

---
### Approach
Dividing an even number by 2 is always optimal. If you change it twice before halving, you could instead halve first and change it once, saving an operation.
Addition or subtraction has more effect on a smaller number, saving more operations.

Odd numbers can also be split into cases.
For $4*n+1$, adding or subtracting one and then halving gives $2*n+1$ or $2*n$, eventually leading to $n+1$ or $n$.
Since we must reach $n$ or $n+1$, subtracting one reaches $n$ in `3` steps, while adding one takes `4`. Reaching $n+1$ takes `4` steps whether we first subtract or add one.
Thus, for $4*n+1$, subtracting one always leads to an answer at least as good as adding one.

Likewise, for $4*n+3$, adding one is better than subtracting one, except for 3: it reaches 1 in two steps, while adding, dividing, and subtracting wastes steps.

### Code

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
            // Combine two steps using the equivalent result after halving, avoiding overflow from adding one to 2^31 - 1
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

Since the correct choice for odd numbers is fully determined, taking min is unnecessary.
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

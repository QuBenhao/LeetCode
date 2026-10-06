# [Python/Java/TypeScript/Go] Arithmetico-geometric sequence + binary search

> slug: pythonjavatypescriptgo-chai-bi-shu-lie-e-nycq
> date: 2022-08-28
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Preimage Size of Factorial Zeroes Function (preimage-size-of-factorial-zeroes-function)
> url: https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/solutions/GWlTkp/pythonjavatypescriptgo-chai-bi-shu-lie-e-nycq/

---
### Approach
1. First, the number of trailing zeros in a factorial depends entirely on its number of factors of 5. Factors of 2 are more plentiful, so only factors of 5 matter.
2. To count the factors of 5 in a factorial, divide the number successively by each power of 5; each power contributes an additional factor of 5.
   The expression above follows the arithmetico-geometric summation formula, except that division is integer division here. We can still bound the number: multiply the original expression by 5 and subtract to show that the number must be at least 4 * k.
3. The number of factors of 5 is nondecreasing as the number grows.
4. An upper bound for a number whose factorial has k factors of 5 is also easy to find: the loose bound 5 * (k + 1) suffices and handles k=0.
5. Binary search within these bounds for a number whose factorial has k factors of 5. Return 0 if none exists; otherwise, the five numbers from x (x % 5 == 0) through x + 4 all qualify.


### Code

```Python3 []
@lru_cache(None)
def dfs(x: int) -> int:
    ans, base = 0, 5
    while x >= base:
        ans += x // base
        base *= 5
    return ans

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # n // 5 + n // 25 + n // 125 + ... = k
        left, right = 4 * k, 5 * (k + 1)
        while left < right:
            mid = (left + right) // 2
            if (d := dfs(mid)) < k:
                left = mid + 1
            elif d == k:
                return 5 
            else:
                right = mid - 1
        return 0
```
```Java []
class Solution {
    private static final Map<Long, Integer> cache = new HashMap<>();

    public int preimageSizeFZF(int k) {
        long left = 4L * k, right = 5L * (k + 1);
        while (left < right) {
            long mid = left + right >> 1;
            int cur = dfs(mid);
            if (cur == k) {
                return 5;
            } else if (cur < k) {
                left = mid + 1L;
            } else {
                right = mid - 1L;
            }
        }
        return 0;
    }

    private int dfs(long x) {
        if (cache.containsKey(x)) {
            return cache.get(x);
        }
        int ans = 0;
        long base = 5L;
        while (x >= base) {
            ans += (int) (x / base);
            base *= 5L;
        }
        cache.put(x, ans);
        return ans;
    }
}
```
```TypeScript []
const cache: Map<bigint, number> = new Map<bigint, number>()
function preimageSizeFZF(k: number): number {
    let left:bigint = 4n * BigInt(k), right: bigint = 5n * (BigInt(k) + 1n)
    while (left < right) {
        const mid: bigint = (left + right) >> 1n
        const cur: number = dfs(mid)
        if (cur == k) {
            return 5
        } else if (cur < k) {
            left = mid + 1n
        } else {
            right = mid - 1n
        }
    }
    return 0
};

function dfs(x: bigint): number {
    if (cache.has(x)) {
        return cache.get(x)
    }
    let ans: number = 0, base: bigint = 5n
    while (x >= base) {
        ans += Math.floor(Number(x / base))
        base *= 5n
    }
    cache.set(x, ans)
    return ans
}
```
```Go []
func preimageSizeFZF(k int) int {
    dfs := func(x int) (ans int) {
        for base := 5; x >= base; base *= 5 {
            ans += x / base
        }
        return
    }
    left, right := 4 * k, 5 * (k + 1)
    for left < right {
        mid := (left + right) >> 1
        cur := dfs(mid)
        if cur == k {
            return 5
        } else if cur < k {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return 0
}

```

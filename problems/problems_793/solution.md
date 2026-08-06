# [Python/Java/TypeScript/Go] 差比数列 + 二分

> slug: pythonjavatypescriptgo-chai-bi-shu-lie-e-nycq
> date: 2022-08-28
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Preimage Size of Factorial Zeroes Function (preimage-size-of-factorial-zeroes-function)
> url: https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/solutions/GWlTkp/pythonjavatypescriptgo-chai-bi-shu-lie-e-nycq/

---
### 解题思路
1. 首先想到的是，阶乘末尾0的个数完全由5的因子个数决定，因为2的个数由于多于5的个数，所以讨论5即可。
2. 其次想到的是计算一个数有多少个5的因子，需要依次除以5的各个次方，每个次方会单独贡献一个额外的5。
   上面的式子和差比求和公式是一致的，不过这里是整除，但是我们仍可得到这个数字的范围。(原式乘以5再作差，会得到该数字一定大于等于4 * k)
3. 5的因子个数是随着数字变大单调不减的。
4. 有k个5的因子的数上界也很容易确定，比较宽松的估一个5 * (k + 1)即可 (兼容k=0的情况)。
5. 在已知的上下界里二分校验有没有数有k个5的因子即可，如果没有返回0，如果有说明该数x (x % 5 == 0)到 x + 4 这五个数都满足。


### 代码

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
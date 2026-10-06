# [Python/Java/JavaScript/Go] Bitmask DP with memoized recursion

> slug: pythonjavajavascriptgo-zhuang-tai-ya-suo-peme
> date: 2022-02-21
> tags: Go, Java, JavaScript, Python, Python3
> question: The Number of Good Subsets (the-number-of-good-subsets)
> url: https://leetcode.cn/problems/the-number-of-good-subsets/solutions/0Ubsud/pythonjavajavascriptgo-zhuang-tai-ya-suo-peme/

---
### Approach

The key constraint is that values are at most 30. Repeated values contribute multiplicities but cannot be selected together. Convert the input to counts, discard multiples of prime squares because they are not square-free, and record the prime factors of each remaining value.&#x20;



Use a bitmask to record selected prime factors. A previously selected prime cannot be selected again: after choosing 6, no other number containing 2 or 3 may be chosen. Equivalently, the factor sets must be disjoint.&#x20;



The value 1 is special: it cannot form a good subset by itself, but choosing any number of 1s, including none, preserves an existing good subset. The recursion therefore returns $2^{cnts[1]}$ at its terminal state.



PS:
Use an array of size 2^10 and update it backward in place to save space.
Remember to handle overflow when multiplying large values.

### Code

```Python3 []
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
FORBID = [p * p for p in PRIMES[:3]]
MOD = int(1e9 + 7)
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        for k in list(cnts.keys()):
            for f in FORBID:
                if not k % f:
                    cnts.pop(k)
        key_primes = defaultdict(set)
        for k in cnts:
            for p in PRIMES:
                if not k % p:
                    key_primes[k].add(p)
                elif k < p:
                    break
        ones = pow(2, cnts[1], MOD)
        
        @lru_cache(None)
        def dfs(idx, ps):
            if idx > 30 or len(ps) == len(PRIMES):
                # Exclude the empty selection with no prime factors chosen
                return (len(ps) > 0) * ones
            st, ans = set(ps), 0
            # idx occurs in the original array and none of its prime factors has been selected
            if idx in cnts and not key_primes[idx] & st:
                ans += cnts[idx] % MOD * dfs(idx + 1, tuple(st | key_primes[idx])) % MOD
            # Add the number of answers that omit idx
            return (ans + dfs(idx + 1, ps)) % MOD

        return dfs(2, tuple())
```
```Java []
class Solution {
    private static final int[] PRIMES = new int[]{2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    private static final int MOD = (int)1e9 + 7;
    private static final Set<Integer> FORBID = new HashSet<>();
    private static final int LEN_POWER = 1 << PRIMES.length;
    static {
        for(int i = 0; i < 3; i++)
            for(int j = PRIMES[i] * PRIMES[i]; j <= 30; j += PRIMES[i] * PRIMES[i])
                FORBID.add(j);
    }

    public int numberOfGoodSubsets(int[] nums) {
        Map<Integer, Integer> cnts = new HashMap<>();
        for(int num: nums)
            if(!FORBID.contains(num))
                cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        Map<Integer, Integer> keyPrimes = new HashMap<>();
        for(int num: cnts.keySet()) {
            int cur = 0;
            for(int i = 0; i < PRIMES.length; i++)
                if(num % PRIMES[i] == 0)
                    cur |= 1 << i;
            keyPrimes.put(num, cur);
        }
        int[] dp = new int[LEN_POWER];
        dp[0] = qpow(2, cnts.getOrDefault(1, 0), (long)MOD);
        for(int i = 2; i <= 30; i++) {
            if(cnts.containsKey(i))
                for(int j = LEN_POWER - 1; j > 0; j--) {
                    int cur = keyPrimes.get(i);
                    if((cur & j) == cur) {
                        dp[j] = (dp[j] + (int)((long)cnts.get(i) * (long)dp[j ^ cur] % MOD)) % MOD;
                    }
                }
        }
        int ans = 0;
        for(int j = 1; j < LEN_POWER; j++)
            ans = (ans + dp[j]) % MOD;
        return ans;
    }

    int qpow(int a, int n, long mod){
        long ans = 1, la = (long)a;
        while(n > 0){
            if((n&1) == 1)
                ans = ans * la % mod;
            la = la * la % MOD;
            n >>= 1;
        }
        return (int)ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
const PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], MOD = 1000000007n,
      FORBID = new Set([4, 8, 12, 16, 20, 24, 28, 9, 18, 27, 25]), LEN_POWER = 1 << PRIMES.length
var numberOfGoodSubsets = function(nums) {
    qpow = function(a, n) {
        let ans = 1n
        while(n > 0) {
            if((n & 1) == 1)
                ans = ans * a % MOD
            a = a * a % MOD
            n >>= 1
        }
        return ans
    }
    const cnts = new Array(31).fill(0n)
    cnts[1] = 0
    for(const num of nums) {
        if(!FORBID.has(num))
            cnts[num]++
    }
    const keyPrimes = new Map()
    for(let num = 2; num <= 30; num++) {
        if(cnts[num] > 0) {
            let cur = 0
            for(let i = 0; i < PRIMES.length; i++) {
                if(num % PRIMES[i] == 0)
                    cur |= 1 << i
                else if(num < PRIMES[i])
                    break
            }
            keyPrimes.set(num, cur)
        }
    }
    const dp = new Array(LEN_POWER).fill(0n)
    dp[0] = qpow(2n, cnts[1])
    for(let i = 2; i <= 30; i++)
        if(keyPrimes.has(i)) {
            const cur = keyPrimes.get(i)
            for(let j = LEN_POWER - 1; j > 0; j--)
                if((cur & j) == cur)
                    dp[j] = (dp[j] + cnts[i] * dp[j ^ cur] % MOD) % MOD
        }
    let ans = 0n
    for(let i = 1; i < LEN_POWER; i++)
        ans = (ans + dp[i]) % MOD
    return ans
};
```
```Go []
const mod int = 1000000007
func numberOfGoodSubsets(nums []int) (ans int) {
    qpow := func(a, n int) int {
        res := int64(1)
        for i := int64(a); n > 0; n >>= 1 {
            if (n & 1 == 1) {
                res = res * i % int64(mod)
            }
            i = i * i % int64(mod)
        }
        return int(res)
    }

    cnts := make([]int, 31)
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    lenPower := 1 << len(primes)
    forbid := map[int]bool{}
    for _, num := range []int{4, 8, 12, 16, 20, 24, 28, 9, 18, 27, 25} {
        forbid[num] = true
    }
    for _, num := range nums {
        if(!forbid[num]) {
            cnts[num] += 1
        }
    }
    keyPrime := map[int]int{}
    for num, v := range cnts {
        if v > 0 {
            cur := 0
            for i, p := range primes {
                if num % p == 0 {
                    cur |= 1 << i
                } else if num < p {
                    break
                }
            }
            keyPrime[num] = cur
        }
    }
    
    dp := make([]int, lenPower)
    dp[0] = qpow(2, cnts[1])
    for i := 2; i <= 30; i++ {
        if(cnts[i] > 0) {
            cur := keyPrime[i]
            for j := lenPower - 1; j > 0; j-- {
                if cur & j == cur {
                    dp[j] = (dp[j] + int(int64(cnts[i]) * int64(dp[j ^ cur]) % int64(mod))) % mod
                }
            }
        }
    }
    for i := 1; i < lenPower; i++ {
        ans = (ans + dp[i]) % mod
    }
    return
}
```

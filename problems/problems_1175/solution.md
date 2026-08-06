# [Python/Java/TypeScript/Go] 欧式筛统计素数个数

> slug: pythonjavatypescriptgo-ou-shi-shai-by-hi-cacg
> date: 2022-06-30
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Prime Arrangements (prime-arrangements)
> url: https://leetcode.cn/problems/prime-arrangements/solutions/Azalkw/pythonjavatypescriptgo-ou-shi-shai-by-hi-cacg/

---
### 解题思路
题目的本意是统计n以内素数的个数，答案由素数的全排列数乘上非素数的全排列数得到。

因此我们只需要统计素数的个数即可。

感谢[@emove](/u/emove/)同学提供的Go语言版本

### 代码

```Python3 []
MOD = int(1e9) + 7
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        return Solution.factorial(cnts := Solution.euler(n)) * Solution.factorial(n - cnts) % MOD

    # 欧式筛统计素数个数
    @staticmethod
    def euler(x):
        is_prime = [True] * (x + 1)
        is_prime[1] = False
        count = 0
        prime = [0] * (x + 1)
        for i in range(2, x + 1):
            if is_prime[i]:
                count += 1
                prime[count] = i
            j = 1
            while j <= count and i * prime[j] <= x:
                is_prime[i * prime[j]] = False
                if not i % prime[j]:
                    break
                j += 1
        return count

    
    @staticmethod
    @lru_cache(None)
    def factorial(x):
        return 1 if x <= 1 else x * Solution.factorial(x - 1) % MOD

```
```Java []
class Solution {
    private static final int MOD = 1000000007;
    private static final int[] PRIMES = new int[101];
    private static final long[] FACTORIAL = new long[101];
    
    static {
        PRIMES[0] = PRIMES[1] = 0;
        FACTORIAL[0] = FACTORIAL[1] = 1L;
        for(int i = 2; i <= 100; i++) {
            FACTORIAL[i] = FACTORIAL[i - 1] * i % MOD;
            PRIMES[i] = PRIMES[i - 1] + (isPrime(i) ? 1 : 0);
        }
    }

    private static boolean isPrime(int x) {
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int numPrimeArrangements(int n) {
        return (int)(FACTORIAL[PRIMES[n]] * FACTORIAL[n - PRIMES[n]] % MOD);
    }
}
```
```TypeScript []
const mem = new Array<bigint>(101).fill(0n), mod = 1000000007n

function numPrimeArrangements(n: number): number {
    const cnts = euler(n)
    return Number(factorial(cnts) * factorial(n - cnts) % mod)
};

function euler(n: number): number {
    const isPrime = new Array<boolean>(n + 1).fill(true), prime = new Array<number>(n + 1).fill(0)
    let count = 0
    isPrime[1] = false
    for (let i = 2; i <= n; i++) {
        if (isPrime[i]) {
            prime[++count] = i
        }
        for (let j = 1; j <= count && i * prime[j] <= n; j++) {
            isPrime[i * prime[j]] = false
            if (i % prime[j] == 0) {
                break
            }
        }
    }
    return count
}

function factorial(n: number): bigint {
    if (n <= 1) {
        return 1n
    }
    if (mem[n] > 0) {
        return mem[n]
    }
    const res = factorial(n - 1) * BigInt(n) % mod
    mem[n] = res
    return res
}
```
```Go []
const MOD = 1e9 + 7

var PRIMES [101]int
var FACTORIAL [101]int64

func init() {
	PRIMES[0], PRIMES[1] = 0, 0
	FACTORIAL[0], FACTORIAL[1] = 1, 1
	for i := 2; i <= 100; i++ {
		FACTORIAL[i] = FACTORIAL[i-1] * int64(i) % MOD
		if isPrime(i) {
			PRIMES[i] = PRIMES[i-1] + 1
		} else {
			PRIMES[i] = PRIMES[i-1] + 0
		}
	}
}

func isPrime(x int) bool {
	for i := 2; i*i <= x; i++ {
		if x%i == 0 {
			return false
		}
	}
	return true
}

func numPrimeArrangements(n int) int {
	return int(FACTORIAL[PRIMES[n]] * FACTORIAL[n-PRIMES[n]] % MOD)
}
```
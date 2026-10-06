# Prime Numbers

Optimization using the [harmonic series](harmonic_series.md)

## Find All Primes up to N

```python
def primes(n):
    n = int(n)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]
```
```cpp
#define MAXN ((int) 1e5)
bool flag[MAXN + 5], inited = false;
void init() {
    if (inited) return;
    inited = true;
    flag[0] = flag[1] = true;
    // Find primes using a sieve
    for (int i = 2; i * i <= MAXN; i++) if (!flag[i]) for (int j = i * 2; j <= MAXN; j += i) flag[j] = true;
}
```
```java
    private static final int MAX_N = 100000;
    private static final boolean[] FLAG = new boolean[MAX_N + 1];
    static {
        FLAG[0] = true;
        FLAG[1] = true;
        for (int i = 2; i * i <= MAX_N; i++) {
            if (!FLAG[i]) {
                for (int j = i * 2; j <= MAX_N; j += i) {
                    FLAG[j] = true;
                }
            }
        }
    }
```

## Count the Distinct Prime Factors of Every Number up to N

```python
def count_distinct_prime_factors(n):
    count = [0] * (n + 1)
    
    for p in range(2, n + 1):
        if count[p] == 0:
            for j in range(p, n + 1, p):
                count[j] += 1
    return count
```

## Prime Factorization

```python
# Precompute the prime factor list for each number
mx = 1000001
PRIME_FACTORS = [[] for _ in range(mx)]
for i in range(2, mx):
    if not PRIME_FACTORS[i]:  # i is prime
        for j in range(i, mx, i):  # Multiples of i have prime factor i
            PRIME_FACTORS[j].append(i)
```
```c++
constexpr int MAX_N = 100000;
array<vector<int>, MAX_N + 1> PRIMES;

bool inited = false;
static void init() {
  if (inited) {
    return;
  }
  for (int i = 2; i <= MAX_N; ++i) {
    if (PRIMES[i].empty()) {
      for (int j = i; j <= MAX_N; j += i) {
        PRIMES[j].push_back(i);
      }
    }
  }
}
```
```golang
const MAX_N = 100000

var PRIMES [][]int

func init() {
	PRIMES = make([][]int, MAX_N+1)
	for i := 2; i <= MAX_N; i++ {
		if len(PRIMES[i]) == 0 {
			for j := i; j <= MAX_N; j += i {
				PRIMES[j] = append(PRIMES[j], i)
			}
		}
	}
}
```
```java
public class Solution {
    private static final int MAX_N = 100000;
    private static List<Integer>[] PRIMES = new List[MAX_N + 1];
    static {
        for (int i = 0; i <= MAX_N; ++i) {
            PRIMES[i] = new ArrayList<>();
        }
        for (int i = 2; i <= MAX_N; ++i) {
            if (PRIMES[i].isEmpty()) {
                for (int j = i; j <= MAX_N; j += i) {
                    PRIMES[j].add(i);
                }
            }
        }
    }
}
```

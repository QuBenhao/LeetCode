# 质数

[调和级数](harmonic_series.md)优化

## 求N以内的所有质数

```python
def primes(n):
    n = int(n)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
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
    // 筛法求质数
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

## 求N以内每个数的不同质因子个数

```python
def count_distinct_prime_factors(n):
    count = [0] * (n + 1)
    
    for p in range(2, n + 1):
        if count[p] == 0:
            for j in range(p, n + 1, p):
                count[j] += 1
    return count
```

## 质因数分解

```python
# 预处理每个数的质因子列表
mx = 1000001
PRIME_FACTORS = [[] for _ in range(mx)]
for i in range(2, mx):
    if not PRIME_FACTORS[i]:  # i 是质数
        for j in range(i, mx, i):  # i 的倍数有质因子 i
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
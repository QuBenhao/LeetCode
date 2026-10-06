# Harmonic Series

The harmonic series often helps reduce algorithmic complexity, especially in problems involving divisors, multiples, or block-based computation. The following example shows how to use its properties to reduce time complexity, with implementations in four languages.

## Classic Application: Count the Divisors of Every Number from 1 to n

### Problem Description
Given a positive integer n, count the divisors of each number i (1 ≤ i ≤ n).

### Brute-Force Solution (O(n√n))
```python
# Python brute-force solution
def count_factors_brute_force(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        count = 0
        # Check every number from 1 to √i
        j = 1
        while j * j <= i:
            if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1
            j += 1
        result[i] = count
    return result
```

### Harmonic Series Optimization (O(n log n))
Use the harmonic series: each number d is a divisor of n/d numbers.

```cpp
// Optimized C++ solution
#include <iostream>
#include <vector>
using namespace std;

vector<int> count_factors(int n) {
    vector<int> factors(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j += i) {
            factors[j]++;
        }
    }
    return factors;
}

int main() {
    int n = 10;
    vector<int> result = count_factors(n);
    for (int i = 1; i <= n; i++) {
        cout << "Number " << i << " has " << result[i] << " factors" << endl;
    }
    return 0;
}
```

```python
# Optimized Python solution
def count_factors(n):
    factors = [0] * (n + 1)
    for i in range(1, n + 1):
        j = i
        while j <= n:
            factors[j] += 1
            j += i
    return factors

n = 10
result = count_factors(n)
for i in range(1, n + 1):
    print(f"Number {i} has {result[i]} factors")
```

```go
// Optimized Go solution
package main

import "fmt"

func countFactors(n int) []int {
    factors := make([]int, n+1)
    for i := 1; i <= n; i++ {
        for j := i; j <= n; j += i {
            factors[j]++
        }
    }
    return factors
}

func main() {
    n := 10
    result := countFactors(n)
    for i := 1; i <= n; i++ {
        fmt.Printf("Number %d has %d factors\n", i, result[i])
    }
}
```

```java
// Optimized Java solution
public class FactorCount {
    public static int[] countFactors(int n) {
        int[] factors = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j += i) {
                factors[j]++;
            }
        }
        return factors;
    }
    
    public static void main(String[] args) {
        int n = 10;
        int[] result = countFactors(n);
        for (int i = 1; i <= n; i++) {
            System.out.println("Number " + i + " has " + result[i] + " factors");
        }
    }
}
```

## Complexity Analysis

1. **Brute-force solution**: O(n√n)
   - For each number i, check √i possible divisors.
   - The total number of operations is approximately n√n.

2. **Harmonic series optimization**: O(n log n)
   - The outer loop runs i from 1 to n.
   - The inner loop starts j at i and increments it by i until it exceeds n.
   - The total number of operations is n(1 + 1/2 + 1/3 + ... + 1/n) ≈ n ln n.

## Other Applications

1. **Sieve of Eratosthenes**: Use the harmonic series to optimize prime sieving.
2. **Divisor summatory function**: Sum the divisor counts of all numbers from 1 to n.
3. **Euler's totient function preprocessing**: Compute totient values for all numbers from 1 to n.
4. **Möbius function preprocessing**: Compute Möbius function values for all numbers from 1 to n.

## Sieve of Eratosthenes Optimization Example

```cpp
// Optimized C++ sieve of Eratosthenes
#include <iostream>
#include <vector>
using namespace std;

vector<bool> sieve_of_eratosthenes(int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return is_prime;
}
```

## Performance Comparison

| Method | Time Complexity | Estimated Runtime for n=10^6 |
|------|------------|--------------------------|
| Brute-force solution | O(n√n) | ~2 seconds |
| Harmonic series optimization | O(n log n) | ~0.1 seconds |

## Summary

The harmonic series approach reduces complexity from O(n√n) to O(n log n) by reversing the iteration: instead of finding divisors for each number, find multiples of each divisor. This optimization is useful for number theory and combinatorics problems, especially when preprocessing large amounts of data.

Key points:
1. Identify the harmonic series structure hidden in the problem.
2. Reverse the iteration and consider the problem from the divisors' perspective.
3. Trade space for time by precomputing results.
4. Consider memory access patterns to improve cache performance.

Understanding this approach helps solve many algorithm problems, especially the preprocessing and optimization problems common in programming contests and interviews.

# 调和级数

调和级数思想常用于优化算法复杂度，特别是在处理涉及因子、倍数或分块计算的问题时。下面我将通过具体题目展示如何利用调和级数性质降低时间复杂度，并提供四种语言的实现。

## 经典应用：计算1~n中每个数的因子个数

### 问题描述
给定正整数n，计算每个数i (1 ≤ i ≤ n) 的因子个数。

### 暴力解法（O(n√n)）
```python
# Python 暴力解法
def count_factors_brute_force(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        count = 0
        # 检查从1到√i的所有数
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

### 调和级数优化解法（O(n log n)）
利用调和级数性质：对于每个数d，它是n/d个数的因子

```cpp
// C++ 优化解法
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
# Python 优化解法
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
// Golang 优化解法
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
// Java 优化解法
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

## 复杂度分析

1. **暴力解法**：O(n√n)
   - 对于每个数i，需要检查√i个可能的因子
   - 总操作数约为n√n

2. **调和级数优化**：O(n log n)
   - 外层循环i从1到n
   - 内层循环j从i开始，每次增加i，直到超过n
   - 总操作数为n(1 + 1/2 + 1/3 + ... + 1/n) ≈ n ln n

## 其他应用场景

1. **埃拉托斯特尼筛法**：利用调和级数思想优化素数筛选
2. **除数函数求和**：计算1~n中所有数的因子个数之和
3. **欧拉函数预处理**：批量计算1~n的欧拉函数值
4. **莫比乌斯函数预处理**：批量计算1~n的莫比乌斯函数值

## 埃氏筛法优化示例

```cpp
// C++ 埃氏筛法优化
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

## 性能对比

| 方法 | 时间复杂度 | n=10^6时的运行时间(估计) |
|------|------------|--------------------------|
| 暴力解法 | O(n√n) | ~2秒 |
| 调和级数优化 | O(n log n) | ~0.1秒 |

## 总结

调和级数思想通过改变循环方向（从"对每个数找因子"变为"对每个因子找倍数"），将算法复杂度从O(n√n)降低到O(n log n)。这种优化技巧在解决数论和组合问题时非常有用，特别是当需要预处理大量数据时。

关键点：
1. 识别问题中隐含的调和级数结构
2. 改变循环方向，从因子角度考虑问题
3. 利用空间换时间，预处理结果
4. 注意内存访问模式，优化缓存性能

掌握这种思想可以帮助解决许多算法问题，特别是在编程竞赛和面试中常见的数据预处理和优化问题。
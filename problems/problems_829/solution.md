# [Python/Java/TypeScript/Go] 数学

> slug: pythonjavatypescriptgo-by-himymben-6n19
> date: 2022-06-03
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Consecutive Numbers Sum (consecutive-numbers-sum)
> url: https://leetcode.cn/problems/consecutive-numbers-sum/solutions/w5miyB/pythonjavatypescriptgo-by-himymben-6n19/

---
### 解题思路
由于要统计的是连续正整数的和，很容易想到用求和公式化简。
$n = \sum_{i=1}^k a_i = a_1 + a_2 + \ldots + a_k = \frac{(a_1 + a_k) * k}{2}$
代入连续正整数的条件:
$n = \frac{(a_1 + a_k) * k}{2} = \frac{(a_1 * 2 + k - 1) * k}{2}$
代入正整数条件($a_1 \ge 1$):
$n = \frac{(a_1 * 2 + k - 1) * k}{2} \ge \frac{(k + 1) * k}{2} \gt \frac{k^2}{2}$
也就是说连续k个正整数的和，我们得到了k的上界。

然后我们根据这个范围遍历统计满足整除关系的次数即可。

附写代码时用注释推导过程
```python3
        # (2 * x + k - 1) * k // 2 = n
        # x >= 1
        # n >= k * (k + 1) // 2
        # x = (2 * n // k + 1 - k) // 2
```

### 代码

```Python3 []
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        return sum(t % i == 0 and (t // i + 1 - i) % 2 == 0 for i in range(1, int(sqrt(t)) + 1)) if (t := 2 * n) else 0
```
```Java []
class Solution {
    public int consecutiveNumbersSum(int n) {
        int t = 2 * n, ans = 0;
        for(int k = 1; k * k < t; k++) {
            if (t % k == 0 && (t / k + 1 - k) % 2 == 0) {
                ans++;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function consecutiveNumbersSum(n: number): number {
    const t = 2 * n
    let ans = 0
    for (let k = 1; k * k < t; k++) {
        if (t % k == 0 && (Math.floor(t / k) + 1 - k) % 2 == 0) {
            ans++
        }
    }
    return ans
};
```
```Go []
func consecutiveNumbersSum(n int) (ans int) {
    for k, t := 1, 2 * n; k * k < t; k++ {
        if t % k == 0 && (t / k + 1 - k) % 2 == 0 {
            ans++
        }
    }
    return
}
```
# [Python/Java/JavaScript/Go] 暴力模拟 -> 素数筛

> slug: pythonjavajavascriptgo-su-shu-shai-by-hi-5i6z
> date: 2022-02-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Simplified Fractions (simplified-fractions)
> url: https://leetcode.cn/problems/simplified-fractions/solutions/Dc1mTb/pythonjavajavascriptgo-su-shu-shai-by-hi-5i6z/

---
### 解题思路
判断每个分子和当前分母的最大公约数是否为1

预处理小于等于n的所有素数，用素数分解枚举的分母的所有质因子，用所有质因子构造分母的所有非互质分子，其他的均可加入答案。

### 代码

```Python3 []
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return ["{}/{}".format(j, i) for i in range(2, n + 1) for j in range(1, i) if gcd(j, i) == 1]
```
```Java []
class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> ans = new ArrayList<>();
        for(int i = 2; i <= n; i++)
            for(int j = 1; j < i; j++)
                if(gcd(i, j) == 1)
                    ans.add(String.format("%d/%d", j, i));
        return ans;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {string[]}
 */
var simplifiedFractions = function(n) {
    gcd = function(a, b) {
        return b == 0 ? a : gcd(b, a % b)
    }
    ans = new Array()
    for(let i = 2; i <= n; i++) 
        for(let j = 1; j < i; j++)
            if(gcd(i, j) == 1)
                ans.push(j + "/" + i) 
    return ans
};
```
```Go []
func simplifiedFractions(n int) (ans []string) {
    for i := 2 ; i <= n; i++ {
        for j := 1; j < i; j++ {
            if gcd(i, j) == 1 {
                ans = append(ans, fmt.Sprintf("%d/%d", j, i))
            }
        }
    }
    return
}

func gcd(a, b int) int {
    if b == 0 {
        return a
    }
    return gcd(b, a % b)
}
```
```python3
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        isPrime = [True] * (n + 1)
        primes = []
        for i in range(2, n + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
                primes.append(i)
        ans = []
        # 枚举分母
        for i in range(2, n + 1):
            if isPrime[i]:
                ans += ["{}/{}".format(j, i) for j in range(1, i)]
            else:
                idx, ps = 0, set()
                # 分母的所有质因子
                while idx < len(primes) and primes[idx] < i // 2 + 1:
                    if not i % primes[idx]:
                        ps.add(primes[idx])
                    idx += 1
                s = set()
                # 构造分母的所有最大公约数不为1的分子
                for p in ps:
                    for j in range(p, i, p):
                        s.add(j)
                ans += ["{}/{}".format(j, i) for j in range(1, i) if j not in s]
        return ans
```
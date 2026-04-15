# [Python] 使用哈希表统计

> Author: Benhao
> Date: 2021-07-07
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路
统计完一个Counter后，遍历每个数字能组成的2的幂($2^0$直到$2^{21}$)，然后用 这个数字的个数 乘上 2的幂减去这个数的个数 就能得到 组成该2的幂个数 了。
注意这个数本身是一个2的幂的一半时，自身构成用组合公式n个里面选两个。

因为总是重复计算了一遍，所以最终结果除2

<br>
另附不重复的加法叠加解法

### 代码

```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        return (sum(cnts[key] * (cnts[key] - 1) if key == 2 ** (i-1) else cnts[key] * cnts[2**i-key] for key in cnts for i in range(22))//2) % (10 ** 9 + 7)
```
这两段代码是等价的，第一个只是写成了一行
```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        ans = 0
        for key in cnts:
            for i in range(22):
                if key == 2 ** (i-1):
                    ans += cnts[key] * (cnts[key] - 1)
                else:
                    ans += cnts[key] * cnts[2**i - key]
        return (ans // 2) % (10 ** 9 + 7)
```
可以避免重复计算22个2的幂来加速(其实还可以循环从key的大小开始来加速)
```python3
class Solution:
    powersOfTwo = [2**i for i in range(22)]
    mod = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        return (sum(cnts[key] * (cnts[key] - 1) if key == target - key else cnts[key] * cnts[target-key] for key in cnts for target in self.powersOfTwo))//2 % self.mod
```
加法叠加
```python3
class Solution:
    powersOfTwo = [2**i for i in range(22)]
    mod = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        cnts, ans = Counter(), 0
        for num in deliciousness:
            for target in self.powersOfTwo:
                ans += cnts[target - num]
            cnts[num] += 1
        return ans % self.mod
```
进阶100%解法，思路来自[@DarkArmed](/u/darkarmed/)
```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 1000000007
        count = Counter(deliciousness)

        res = 0
        # 由于每个数只遍历了最接近自己的2的次幂的组合，所以不可能重复;比如说1和3构成4，只在3的时候计算；3和5构成8只在5的时候计算。
        for i in count:
            if i == 0:
                continue
            # i的下一个2的幂次
            target = self.nextPower(i)
            # 如果i能和任意的count中的key够成这个幂次
            res += count[i] * count[target - i]
            # 如果i自身是一个2的幂次
            if i == target:
                res += count[i] * (count[i] - 1) // 2
        return res % MOD

    def nextPower(self, x: int):
        x -= 1
        x |= x >> 1
        x |= x >> 2
        x |= x >> 4
        x |= x >> 8
        x |= x >> 16
        return x + 1
```
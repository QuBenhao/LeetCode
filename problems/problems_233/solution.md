# [Python/Java] 递归求解

> slug: python-di-gui-qiu-jie-by-qubenhao-a3lc
> date: 2021-08-13
> tags: Java, Python, Python3
> question: Number of Digit One (number-of-digit-one)
> url: https://leetcode.cn/problems/number-of-digit-one/solutions/BQai4x/python-di-gui-qiu-jie-by-qubenhao-a3lc/

---
### 解题思路
> 先观察以下规律，
> 9以下的1有`1`个
> 99以下的1相当于从10个9里面取1(个位数)，又从10-19里面的十位数取1,所以是10 + 10*1 = `20`
> 999以下的有 100 + 10 * 20 = `300`
> 以此类推


那么现在给我们一个n,我们首先知道它能出现多少次一个小于等于它的9999..。比如说`3278`，必然是包含了`999`的而且0999,1999,2999一共相当于出现了三次，这就是我们的res部分的`999`中1的个数乘以第一位的大小。这个时候没考虑的是什么呢？一个是第一位为3时其他位变动产生的1以及第一位是1的所有(仅讨论第一位上的1)。

前者正是往后的一个递归了(比如`3278`我们需要知道`278`能组成多少1，它是第一位为`3`的1的个数)，而后者，要讨论是否大于1，这就好比`3278`中是包含`1000-1999`的所有千位数的1的，但是`1278`中只有279个千位数的1。所以我们在返回的时候，判断他是不是大于1然后加不同的个数即可。

> 注意：n的第一位是不可能为0的，这是整数的一个性质，所以这保证了我们第一位要么等于1，要么大于1

### 代码

```Python3 []
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 10:
            return 1 if n else 0
        num = str(n)
        x = len(num) - 1
        nxt = int(num[1:])
        res = self.f(x) * int(num[0]) + self.countDigitOne(nxt)
        # 第一位大于1，包含那位为1的所有1的个数是10**x ; 否则是num后面的部分再加上"10000.."这个情况的1
        return res + 10 ** x if int(num[0]) > 1 else res + nxt + 1

    """
    0-9: 1
    0-99: 10 + 10 * 1 = 20
    0-999: 100 + 10 * 20 = 300
    0-9999: 1000 + 10 * 300 = 4000
    0-99999: 10000 + 10 * 4000 = 50000
    f(i) = 10 ** (i-1) + 10 * f(i-1)
    其实也可以直接写 f(i) = i * 10 ** (i-1)
    """
    @lru_cache(None)
    def f(self, i):
        # return i * 10 ** (i-1)
        return 10 ** (i-1) + 10 * self.f(i-1) if i else 0
```
```Java []
class Solution {
    // dp[i] = i * (int)Math.pow(10, i-1);
    int[] dp = new int[]{0,1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000};
    public int countDigitOne(int n) {
        if(n < 10)
            return n == 0 ? 0 : 1;
        String num = String.valueOf(n);
        int length = num.length() - 1, first = num.charAt(0) - '0';
        int firstNum = (int)Math.pow(10, length);
        int nxt = n - firstNum * first;
        return first > 1 ? countDigitOne(nxt) + dp[length] * first + firstNum : countDigitOne(nxt) + dp[length] * first + nxt + 1;
    }
}
```

### 复杂度
分析: 递归的时候，我们每次处理了最左位的数字，递归的时候减去了这一位，数字大小可以大概认为是除以10的(下次至少少一位)，所以:
时间复杂度 $o(log_{10}n)$
空间复杂度 $o(log_{10}n)$
更准确地应该写成n中不为0的位数。
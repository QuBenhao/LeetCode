# [Python/Java] 记忆化递归

> Author: Benhao
> Date: 2021-09-11
> Upvotes: 20
> Tags: Java, Python, Python3

---

### 解题思路
随便给我们一个二进制数字(也就是n): 10110，我们能有多少个不连续的数字组合其实就像是不选相邻房子的打家劫舍。
所有小于等于n的数，我们考虑第一位，他要么是1，要么是0。

> 如果第一位取1，那么为了满足条件，第二位必须是0，如果原来第二位就是0，那么后面的位数最大就能取到抛去前两位的递归，也就是110里面取出的个数(这样才小于n)。
> 而如果第二位是1，由于第一位取1所以必须取0，但是后面怎么取都会比n小了，所以可以往后面全是1里面递归，也就是111。
> 如果第一位取0，相当于往1111里递归。


### 代码

```Python3 []
class Solution:
    @lru_cache(None)
    def findIntegers(self, n: int) -> int:
        if n <= 3:
            return n + 1 if n < 3 else n
        bits = len(bin(n)) - 2
        return self.findIntegers((1<<(bits-1))-1) + (self.findIntegers((1<<(bits-2))-1) if (n >> (bits - 2)) & 1 else self.findIntegers(n - (1<<(bits-1))))
```
```Java []
class Solution {
    HashMap<Integer, Integer> dp = new HashMap<>();
    public int findIntegers(int n) {
        if(n < 4)
            return n < 3 ? n + 1 : n;
        if(dp.containsKey(n))
            return dp.get(n);
        int b = bits(n);
        // 第一位取0的个数
        int res = findIntegers((1 << b) - 1);
        // 根据第二位是不是1判断第一位取1的个数
        res += ((n >> (b - 1)) & 1) == 1? findIntegers((1 << (b-1)) - 1) : findIntegers(n - (1 << b));
        dp.put(n, res);
        return res;
    }

    public int bits(int n){
        for(int i = 31; i > 0; i--)
            if(((n >> i) & 1) == 1)
                return i;
        return 0;
    }
}
```


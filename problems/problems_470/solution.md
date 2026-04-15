# [Python/Java] 分享一下lee神的期望1.183次rand7

> Author: Benhao
> Date: 2021-09-05
> Upvotes: 11
> Tags: Java, Python, Python3

---

### 解题思路
官方题解或者其他解法都是很棒的思路，但是他们都舍弃太多random出来的数了，导致最终的调用期望次数很高。而理论上最佳的期望为$log_{7}10 = 1.183$，而这个期望正是需要[lee215的题解](https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C%2B%2BJavaPython-1.183-Call-of-rand7-Per-rand10)
的7的次方思路的。

我的理解哈。$7^{19} = 11398895185373143$。就如同生成49舍弃40-48时一样，这里舍弃后能保证11398895185373140种情况生成了（至少）一个随机数，概率是99.99999999999997%。而且其中10000000000000000以下的数是一个16位的10进制数，而这16位数每位数0-9的概率是一致的，也就是87.73%的概率生成了16个随机数。

没有特别理解清楚这个解法，希望有大佬指教。

### 代码

```Python3 []
class Solution:
    cache, upper = 0, 1
    def rand10(self):
        while self.upper < 10**9:
            self.cache, self.upper = self.cache * 7 + rand7() - 1, self.upper * 7
        res = self.cache % 10 + 1
        self.cache, self.upper = self.cache // 10, self.upper // 10
        return res
```
```Java []
class Solution extends SolBase {
    long cache = 0L, range = 1L;
    public int rand10() {
        while(range < 1e9){
            cache = cache * 7 + rand7() - 1;
            range *= 7;
        }
        long tmp = cache;
        cache /= 10;
        int res = (int)(tmp - cache * 10) + 1;
        range /= 10;
        return res;
    }
}
```
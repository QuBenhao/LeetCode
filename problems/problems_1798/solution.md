# [Python] 排序前缀和思路过程详解

> Author: Benhao
> Date: 2021-03-21
> Upvotes: 2
> Tags: Python

---

### 解题思路
首先因为题目是要从小到大建立，首先想到排序，因为造小的数字要用小的数，大的数不可能用得到；
一个数组能造出来的最大的数是他们的和，那么每一段能达到的最大的数就是他们的前缀和，想到用persum来计算，实际上也可以算出来；如果现在能造到刚好是当前的和，那么去尝试下一个数，如果coins[i] <= ans也就代表利用coins[i]和之前的造法可以达到从coins[i]直到coins[i] + persum[i-1] (因为之前的造法就是连续的，所以之间的都能连续构成)，也就是persum[i].

实际上直到发现coins[i] > ans的时候，我们无法构造出当前的ans了，因为之前只能构造到persum[i-1],coins[i]又太大了，无法造出persum[i-1]+1了。

然后发现ans本身就可以取代前缀和，ans其实就是前缀和，那么代码就可以简化成第二段了。

### 代码

```python
class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        persum = [0] * len(coins)
        ans = 1
        for i,c in enumerate(coins):
            persum[i] += persum[i-1] + c

        if persum[0] != 1:
            return ans
        ans += 1
        for i in range(1,len(persum)):
            if persum[i] == ans:
                ans += 1
            elif coins[i] <= ans:
                ans = persum[i] + 1
            else:
                return ans
        return ans
```

简化后
```python
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ans = 1
        for coin in sorted(coins):
            if coin <= ans:
                ans += coin
            else:
                return ans
        return ans
```
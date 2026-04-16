# [Python] 前缀和变量+字典

> Author: Benhao
> Date: 2021-06-03
> Upvotes: 54
> Tags: Python, Python3

---

### 解题思路
使用字典记录每个`1的数量和0的数量的差值`最早出现的位置,使用前缀和变量统计从开始到现在的`1的数量和0的数量的差值`。


为什么这么做呢？先不考虑最长的问题。
想一想如果两个位置的`1的数量和0的数量的差值`相等，意味着什么？
假设这个差值是`k`,左边位置`x`有`m`个0,可知`x`有`m+k`个1（保证数量差值为k）；同时假设右边位置`y`有`n`个0，可知`y`有`n+k`个1。
那么可以知道(x,y]（左开右闭）里，`0`的数量为`n-m`,`1`的数量为`n+k-m-k=n-m`，
故**满足1和0数量的差值相等的两个位置 的充分必要条件是: 他们之间0和1的数量相同**。


那么现在要想找最长，我们肯定希望左边的位置尽可能靠左，所以我们在更新的时候，出现在字典中的相同值不再更新！只是统计一下长度大小。

### 代码

```python3
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        hashmap = {0:-1}
        # 当前1的数量和0的数量的差值
        counter = ans = 0
        for i,num in enumerate(nums):
            # 每多一个1，差值+1
            if num:
                counter += 1
            # 每多一个0，差值-1
            else:
                counter -= 1
            # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等！
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans

```
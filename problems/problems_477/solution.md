# [Python] 统计每一位有多少个0，有多少个1

> Author: Benhao
> Date: 2021-05-28
> Upvotes: 12
> Tags: Python, Python3

---

### 解题思路
> 第一段代码
> 使用一个Counter来记录每一位`1`的个数，这样是循环到每个数的时候既可以统计和前面的数的汉明距离，又可以更新Counter。

> 第二段代码是去掉了循环中的统计汉明距离，直接在最终对每一位统计`0`的个数乘以`1`的个数。这里其实是把刚刚的`循环加法`换成了一个`乘法求和`。
> 每位`0`的个数是总共的数字个数减去`1`的个数。

> 有了第二段代码不难发现
> 我们只需要知道每一位的`0`和`1`的个数，这和昨天使用bin(x).count('1')是一致的。
> 我们需要`map`+`bin`获得所有数字的二进制字符串，然后统计每一位的'1'即可。这刚好就是`zip`的拆分。
> 取30位是因为2^29 < 10^9 < 2^30

**关于format**
将十进制转换为固定长度的多进制类型：
> `8位二进制`
> '{:08b}'.format(9)
> '00001001'

> `6位8进制`
> '{:06o}'.format(9)
> '000011'

>`6位16进制`
> '{:06x}'.format(9)
> '000009'


### 代码

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        trie = Counter()
        max_bit = len(bin(max(nums))) - 2
        ans = 0
        for i, num in enumerate(nums):
            for j in range(max_bit):
                bit = (num >> j) & 1
                if bit:
                    ans += i - trie[j]
                    trie[j] += 1
                else:
                    ans += trie[j]
        return ans
```

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        trie = Counter()
        max_bit = len(bin(max(nums))) - 2
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(max_bit):
                if (num >> j) & 1:
                    trie[j] += 1
        return sum(trie[i] * (n - trie[i]) for i in range(max_bit))
```

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum((ones:= s.count('1')) * (len(nums) - ones) for s in zip(*map('{:30b}'.format, nums)))
```
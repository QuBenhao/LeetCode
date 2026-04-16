# [Python] 三种思路

> Author: Benhao
> Date: 2021-07-03
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
第一种看起来很花里胡哨，实际上思路很朴素(速度也慢)。重复的数是唯一一个有两个的所以是most_common(1)，而丢失的数是全部的数的集合减去现有的集合。
<br>
第二种是数学思路，1到n应该的和为(n+1)*n//2, 实际的和为sum(nums), 去重后的和为sum(set(nums))。很显然实际的和减去去重的和就是唯一的一个重复的数，应该的和减去我们去重的和(出现了的数)就是唯一一个没出现的数了。
<br>
第三种使用位运算(最省空间)。我们很容易求得1到n的异或以及nums的全部异或。这两个结果的异或就是重复的数和缺失的数的异或了。然后参考了一下[这个代码](https://leetcode.com/problems/set-mismatch/discuss/105513/XOR-one-pass)的负数标记法来找到重复的数。

### 代码

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 左边是重复的数，右边是丢失的数
        return [Counter(nums).most_common(1)[0][0], (set(i for i in range(1, len(nums) + 1)) - set(nums)).pop()]

```

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # # 左边是重复的数，右边是丢失的数        
        # x = sum(nums) - sum(set(nums))
        # sum(nums) = x + 1 + ... + n - y
        # y = x + 1 + ... + n - sum(nums) = x + n * (n+1)//2 - sum(nums) = n * (n+1) // 2 - sum(set(nums))
        n, s = len(nums), sum(set(nums))
        return [sum(nums) - s, n * (n + 1) // 2 - s]
```

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 1 ^ 2 ^ ... ^ 4k = 4k
        # 1 ^ 2 ^ ... ^ 4k+1 = 4k ^ 4k+1 = 1
        # 1 ^ 2 ^ ... ^ 4k+2 = 4k+2 ^ 1 = 4k+3
        # 1 ^ 2 ^ ... ^ 4k+3 = 0
        n = len(nums)
        # 应该的位运算结果
        ans = [n, 1, n+1, 0][n%4]
        # 实际的位运算结果以及重复的数字
        res = repeat = 0
        for num in nums:
            val = abs(num)
            res ^= val
            if nums[val-1] < 0:
                repeat = val
            else:
                nums[val-1] = -nums[val-1]
        # res的结果少异或了一次丢失的数, 多异或了一次重复的数，也就是说res^ans=x^y
        return [repeat, repeat ^ res ^ ans]
```
# [Python] 从双重循环到一重循环

> Author: Benhao
> Date: 2021-05-18
> Upvotes: 6
> Tags: Python, Python3

---

### 解题思路
**核心**
注意到 `2^3 = 1`时同样有`2 = 3^1`,
也就是满足`a^b^c = d`的时候, 也会满足`a^b = c^d`和`a = b^c^d`。
对于满足`arr[i] ^ arr[i+1] ^ ... ^ arr[k] = 0` 的`i,k`，任意的在`[i+1,k]`区间的`j`都可以构成一个数目，
那么`[i+1,k]`的区间一共有`k-i`种选择，故对于`i,k`来说有`k-i`个j可以作为答案。

那么我们统计之前的所有异或和（区间到数组的前一个值的异或），和当前的值相等时，我们在乎的是`哪些坐标满足异或值等于当前值`。
如果统计满足异或值为`m`的列表中每个坐标，我们只需要用`len(list) * k - sum(list)`即可更新右边界为`k`的所有答案。

**二重到一重**
统计上一轮的所有异或和，无外乎还是要统计异或前缀。因为上一轮的`num[i] ^ num[i+1] ^ ... num[k-1] = prexor[i] ^ prexor[k]`,
也就是如果存在prexor[i]与当前异或结果相同，就找到了一组`i,k`，只需要记录所有满足`prexor[i] = prexor[k]`的`i`即可实现上面的更新。

### 代码

```python3
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # hashmap = defaultdict(list)
        # ans = 0
        # for j, num in enumerate(arr):
        #     new = defaultdict(list)
        #     for key, val in hashmap.items():
        #         # 如果hashmap中存在与当前num相等的key，满足答案，
        #         # 他们之间的任意一个除最左边外的坐标作为j, 都满足条件
        #         if key == num:
        #             ans += j * len(val) - sum(val)
        #         new[num ^ key] = val
        #     new[num].append(j)
        #     hashmap = new
        # return ans

        l, s = Counter(), Counter()
        prexor = ans = 0
        for k, num in enumerate(arr):
            # 将之前的异或结果更新
            l[prexor] += 1
            s[prexor] += k
            # curxor = arr[0] ^ arr[1] ^ ... ^ arr[k]
            prexor ^= num
            # 之前存在任意的i满足：arr[0] ^ arr[1] ^ ... ^ arr[i] = curxor,
            # 那么i到k可以构成一个异或为0的解，他们之间任意一个坐标(除i以为可以作为j)
            if prexor in l:
                # 同上面的双重循环解法, 利用数量和坐标距离更新
                ans += k * l[prexor] - s[prexor]
        return ans

```
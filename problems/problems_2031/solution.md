# [Python] 学习一下O(n)解法

> slug: by-himymben-vl4n
> date: 2022-05-04
> tags: Python, Python3
> question: Count Subarrays With More Ones Than Zeros (count-subarrays-with-more-ones-than-zeros)
> url: https://leetcode.cn/problems/count-subarrays-with-more-ones-than-zeros/solutions/CEgCcJ/by-himymben-vl4n/

---
### 解题思路
用一个变量维护满足条件的子数组总数，每次变化+1和-1的时候维护变化的波动值。

### 代码

```python3
MOD = int(1e9) + 7
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # 前缀和的个数
        cnts = Counter()
        cnts[0] = 1
        # cnt 维护所有满足条件的子数组个数（因为每次只有+1和-1的变化，所以每次只看边界波动值即可）
        ans = cnt = s = 0
        for num in nums:
            if num:
                # 前缀和为s的个数，当前和将要加一，所以所有和为s的前缀个数均可和当前值构成一个答案子数组
                cnt += cnts[s]
                s += 1
            else:
                # 前缀和为s + 1的个数，当前和将要减一，所以所有和为s + 1的前缀个数均不再能构成一个答案子数组
                s -= 1
                cnt -= cnts[s]
            cnts[s] += 1
            ans = (ans + cnt) % MOD
        return ans
```
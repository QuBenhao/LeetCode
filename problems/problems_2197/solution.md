# [Python] 栈模拟

> Author: Benhao
> Date: 2022-03-06
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
不停的判断相邻的最大公约数是否大于1，大于1就合并。
和答案栈的最后一个同样要比较（向左合并）

### 代码

```python3
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        cur, i = 1, 0
        while i < len(nums):
            has = False
            if gcd(nums[i], cur) == 1:
                cur = nums[i]
            while i < len(nums) and gcd(nums[i], cur) > 1:
                cur = lcm(nums[i], cur)
                i += 1
                has = True
            while ans and gcd(ans[-1], cur) > 1:
                cur = lcm(ans.pop(), cur)
            ans.append(cur)
            if not has:
                i += 1
        return ans
```
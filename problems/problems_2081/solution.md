# [Python] 下一个对称数枚举 + 进制转换

> Author: Benhao
> Date: 2021-11-21
> Upvotes: 5
> Tags: Python, Python3

---

### 解题思路
枚举对称数，再转换进制，再检查转换后是否对称即可

### 代码

```python3 []
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def nxt_rev(cur):
            s = str(cur)
            if len(s) % 2:
                l = r = len(s) // 2
            else:
                r = len(s) // 2
                l = r - 1
            while l >= 0 and s[l] == '9':
                l -= 1
                r += 1
            if l == -1:
                return 10 ** len(s) + 1
            elif l == r:
                return int(s[:l] + str((int(s[l]) + 1)) + s[r + 1:])
            return int(s[:l] + str((int(s[l]) + 1)) + '0' * (r - 1 - l) + str((int(s[r]) + 1)) + s[r + 1:])


        # 十进制转换为base进制
        def convert_to_base(num, base):
            ans = []
            while num:
                ans.append(str(num % base))
                num //= base
            return "".join(ans[::-1])


        def is_rev(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = 1
        cur = 1
        n -= 1
        while n:
            cur = nxt_rev(cur)
            if is_rev(convert_to_base(cur, k)):
                ans += cur
                n -= 1
        return ans
```
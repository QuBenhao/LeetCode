# [Python] 偷懒使用permutations (一行)，面试记住递归和非递归两种解法

> slug: python-permutations-by-qubenhao-3yqy
> date: 2021-06-21
> tags: Python, Python3
> question: 套餐内商品的排列顺序 (zi-fu-chuan-de-pai-lie-lcof)
> url: https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/solutions/jglzap/python-permutations-by-qubenhao-3yqy/

---
### 解题思路
permutations本身就是序列的全排列，但是不会去重，加上set即可。

**递归**
递归的思路很简单，每次从列表中取一个放在最前面，然后和后面的全排列组合即可。（因为有很多重复计算，所以加入记忆化可以从500ms优化到100ms）

**非递归**
非递归相对麻烦，可以考虑字典序解全排列(按从最小到最大生成).
记得之前周赛还是什么时候做过类似19631的下一个刚好比它大一点的排列的数是什么（非递归解决这个问题）。
想象1234是最小的，下一个是1243，再下一个是1324，。。。以此类推。

### 代码

```python3
class Solution:
    def permutation(self, s: str) -> List[str]:
        return list(set(''.join(st) for st in itertools.permutations(s)))
```
递归解法
```python3
class Solution:
    @lru_cache(None)
    def permutation(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]
        return list(set(s[i] + perm for i in range(len(s)) for perm in self.permutation(s[:i] + s[i+1:])))
```
非递归解法
```python3
class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        curr = list(sorted(s))
        end = list(reversed(curr))
        ans = []
        # 生成下一个排列
        while curr != end:
            ans.append(''.join(curr))
            i = n - 2
            # 29631 -> 31269
            while i > 0 and curr[i] >= curr[i+1]:
                i -= 1
            j = n - 1
            while j > i-1 and curr[j] <= curr[i]:
                j -= 1
            curr[i], curr[j] = curr[j], curr[i]
            curr = curr[:i+1] + sorted(curr[i+1:])
        ans.append(''.join(end))
        return ans
```
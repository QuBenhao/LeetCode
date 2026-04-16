# [Python] 单调栈

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
逆序维护一个单调栈。

每个高度的人在踢掉栈里的元素时(从小到大)，这些全部都是他能看到的人，栈里如果剩下还有比他高的，他只能看到那个人，再往后的看不到了。

### 代码

```python3
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        min_stack = []
        for i in range(n-1, -1, -1):
            h = heights[i]
            count = 0
            while min_stack and min_stack[-1] < h:
                min_stack.pop()
                count += 1
            if len(min_stack):
                count += 1
            ans[i] = count
            min_stack.append(h)
        return ans

```
# [Python] 单调栈

> slug: python-by-himymben-xbbz
> date: 2022-10-21
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Online Stock Span (online-stock-span)
> url: https://leetcode.cn/problems/online-stock-span/solutions/2yU9NN/python-by-himymben-xbbz/

---
### 解题思路
栈内只维护比自己大的元素，弹出所有小于等于自身的元素，在弹出时叠加他们的连续长度即可（小于等于他们肯定也小于等于当前元素）。
可以想象成每次最大连续日数都被压缩了，比如`[100, 80, 60, 70]` 会变成 `[100, 80, 70(长度2)]`, 这样下一个包括70的元素就自动包含了他的长度2


### 代码

```python3
class StockSpanner:

    def __init__(self):
        self.stack = [(0, inf)]

    def next(self, price: int) -> int:
        ans = 0
        while self.stack and self.stack[-1][1] <= price:
            ans += self.stack.pop()[0]
        self.stack.append((ans + 1, price))
        return ans + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```
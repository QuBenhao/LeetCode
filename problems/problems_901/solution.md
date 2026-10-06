# [Python] Monotonic stack

> slug: python-by-himymben-xbbz
> date: 2022-10-21
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Online Stock Span (online-stock-span)
> url: https://leetcode.cn/problems/online-stock-span/solutions/2yU9NN/python-by-himymben-xbbz/

---
### Approach
Keep only elements larger than the current one in the stack. Pop all elements less than or equal to it and accumulate their consecutive spans; anything at most those elements is also at most the current one.
Think of each maximal consecutive span as compressed: `[100, 80, 60, 70]` becomes `[100, 80, 70(span 2)]`, so a later element that includes 70 automatically includes its span of 2


### Code

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

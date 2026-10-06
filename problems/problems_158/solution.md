# [Python] Understanding the problem took some effort (99%)

> slug: python-hen-ma-fan-di-li-jie-liao-ti-mu-b-290i
> date: 2021-08-21
> tags: Python, Python3
> question: Read N Characters Given read4 II - Call Multiple Times (read-n-characters-given-read4-ii-call-multiple-times)
> url: https://leetcode.cn/problems/read-n-characters-given-read4-ii-call-multiple-times/solutions/nSeDt3/python-hen-ma-fan-di-li-jie-liao-ti-mu-b-290i/

---
### Approach
Recursive solution: when the buffer is insufficient, read four more characters into it.

### Code

```python3
class Solution:
    def __init__(self):
        self.buf = deque([])

    def read(self, buf: List[str], n: int) -> int:
        if not n:
            return n
        if not self.buf:
            tmp = [''] * 4
            length = read4(tmp)
            if not length:
                return 0
            for i in range(length):
                self.buf.append(tmp[i])
        idx = 0
        while self.buf:
            buf[idx] = self.buf.popleft()
            idx += 1
            if idx == n:
                return n          
        require = n - idx
        res = [''] * require
        self.read(res, require)
        for c in res:
            buf[idx] = c
            idx += 1
        return idx
```

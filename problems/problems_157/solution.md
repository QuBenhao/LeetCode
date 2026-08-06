# [Python] 模拟

> slug: python-mo-ni-by-himymben-mzdo
> date: 2021-08-21
> tags: Python, Python3
> question: Read N Characters Given Read4 (read-n-characters-given-read4)
> url: https://leetcode.cn/problems/read-n-characters-given-read4/solutions/5jg9WG/python-mo-ni-by-himymben-mzdo/

---
```python3
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while True:
            tmp = [''] * 4
            length = read4(tmp)
            for i in range(length):
                buf[idx] = tmp[i]
                idx += 1
                if idx == n:
                    return n
            if length < 4:
                return idx
```
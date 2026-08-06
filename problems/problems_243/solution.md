# [Python] 暴力

> slug: python-bao-li-by-himymben-eog0
> date: 2021-08-22
> tags: Python, Python3
> question: Shortest Word Distance (shortest-word-distance)
> url: https://leetcode.cn/problems/shortest-word-distance/solutions/39x5XR/python-bao-li-by-himymben-eog0/

---
```python3
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = pos2 = None
        ans = inf
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i
            if pos1 is not None and pos2 is not None:
                ans = min(ans, abs(pos1 - pos2))
        return ans
```
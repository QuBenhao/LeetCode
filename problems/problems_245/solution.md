# [Python] 分类讨论暴力

> slug: python-fen-lei-tao-lun-bao-li-by-himymbe-fi7c
> date: 2021-08-22
> tags: Python, Python3
> question: Shortest Word Distance III (shortest-word-distance-iii)
> url: https://leetcode.cn/problems/shortest-word-distance-iii/solutions/eJmNJ6/python-fen-lei-tao-lun-bao-li-by-himymbe-fi7c/

---
```python3
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        def normal():
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
        if word1 != word2:
            return normal()
        last = None
        ans = inf
        for i, word in enumerate(wordsDict):
            if word == word1:
                if last is not None:
                    ans = min(ans, i - last)
                last = i
        return ans

```
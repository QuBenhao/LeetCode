# [Python] 暴力

> slug: python-bao-li-by-himymben-qao0
> date: 2021-08-22
> tags: Python, Python3
> question: Shortest Word Distance II (shortest-word-distance-ii)
> url: https://leetcode.cn/problems/shortest-word-distance-ii/solutions/F01yeE/python-bao-li-by-himymben-qao0/

---
```python3
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.dict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        return min(abs(p1 - p2) for p1 in self.dict[word1] for p2 in self.dict[word2])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
```
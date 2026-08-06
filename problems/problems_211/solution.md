# [Python]  Trie + BFS

> slug: python-trie-bfs-by-himymben-m90f
> date: 2024-03-10
> tags: C, Go, Java, Python3, TypeScript
> question: Design Add and Search Words Data Structure (design-add-and-search-words-data-structure)
> url: https://leetcode.cn/problems/design-add-and-search-words-data-structure/solutions/1glRPJ/python-trie-bfs-by-himymben-m90f/

---
### 解题思路
Trie树，在搜索时用BFS处理"."的情况

### 代码

```Python3 []
class WordDictionary:

    def __init__(self):
        self.root = {}


    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = {}


    def search(self, word: str) -> bool:
        word += "#"
        queue = deque([self.root])
        for c in word:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if c == ".":
                    for v in node.values():
                        queue.append(v)
                elif c in node:
                    queue.append(node[c])
            if not queue:
                return False
        return True



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
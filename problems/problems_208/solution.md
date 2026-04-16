# [Python] 字典Trie模版

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---

### 解题思路
Trie

### 代码

```Python3 []
class Trie:

    def __init__(self):
        self.root = {}


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = True    

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
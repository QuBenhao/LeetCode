# Trie

```python3
root = {}


def insert(word):
    node = root
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = True


def search(word):
    node = root
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '#' in node


def starts_with(prefix):
    node = root
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True
```

```go
package main

type TrieNode struct {
    children map[rune]*TrieNode
    isEnd    bool
}

func TrieNodeConstructor() *TrieNode {
    return &TrieNode{children: make(map[rune]*TrieNode)}
}

func (t *TrieNode) Insert(word string) {
    node := t
    for _, char := range word {
        if _, exists := node.children[char]; !exists {
            node.children[char] = TrieNodeConstructor()
        }
        node = node.children[char]
    }
    node.isEnd = true
}

func (t *TrieNode) Search(word string) bool {
    node := t
    for _, char := range word {
        if _, exists := node.children[char]; !exists {
            return false
        }
        node = node.children[char]
    }
    return node.isEnd
}

func (t *TrieNode) StartsWith(prefix string) bool {
    node := t
    for _, char := range prefix {
        if _, exists := node.children[char]; !exists {
            return false
        }
        node = node.children[char]
    }
    return true
}
```
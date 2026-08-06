# [Python/Java/JavaScript/Go] Trie + DFS or BFS

> slug: pythonjavajavascriptgo-trie-dfs-or-bfs-b-cbmd
> date: 2021-11-13
> tags: Go, Java, JavaScript, Python, Python3
> question: Map Sum Pairs (map-sum-pairs)
> url: https://leetcode.cn/problems/map-sum-pairs/solutions/EfOlbr/pythonjavajavascriptgo-trie-dfs-or-bfs-b-cbmd/

---
### 解题思路
常规的Trie树(还不了解Trie的同学可以先看三叶的前置🧀：[实现 Trie (前缀树)](https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247488490&idx=1&sn=db2998cb0e5f08684ee1b6009b974089&chksm=fd9cb8f5caeb31e3f7f67dba981d8d01a24e26c93ead5491edb521c988adc0798d8acb6f9e9d&token=59039721&lang=zh_CN#rd))，
在结束符号存val，这样相同的单词就会更新存储的val。
在DFS或BFS搜前缀的所有值时，统计所有节点下的“#”的值的和。

### 代码
DFS
```Python3 []
class MapSum:

    def __init__(self):
        self.trie = dict()

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for k in key:
            if k not in node:
                node[k] = dict()
            node = node[k]
        node["#"] = val

    def sum(self, prefix: str) -> int:
        node = self.trie
        for k in prefix:
            if k not in node:
                return 0
            node = node[k]
        return self.dfs(node)
    
    def dfs(self, node):
        ans = 0
        for k in node:
            if k == '#':
                ans += node[k]
            else:
                ans += self.dfs(node[k])
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```
```Java []
class MapSum {
    private Trie root;
    public MapSum() {
        root = new Trie();
    }
    
    public void insert(String key, int val) {
        Trie node = root;
        for(int i=0;i<key.length();i++){
            char c = key.charAt(i);
            if(!node.map.containsKey(c))
                node.map.put(c, new Trie());
            node = (Trie)node.map.get(c);
        }
        node.map.put('#', val);
    }
    
    public int sum(String prefix) {
        Trie node = root;
        for(int i=0;i<prefix.length();i++){
            char c = prefix.charAt(i);
            if(!node.map.containsKey(c))
                return 0;
            node = (Trie)node.map.get(c);
        }
        return dfs(node);
    }

    public int dfs(Trie node) {
        int ans = 0;
        for(char k:node.map.keySet()){
            if(k == '#')
                ans += (int)node.map.get(k);
            else
                ans += dfs((Trie)node.map.get(k));
        }
        return ans;
    }

    class Trie{
        Map<Character, Object> map;
        public Trie(){
            map = new HashMap<>();
        }
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```
```JavaScript []
var MapSum = function() {
    this.root = new Map();
};

/** 
 * @param {string} key 
 * @param {number} val
 * @return {void}
 */
MapSum.prototype.insert = function(key, val) {
    let node = this.root;
    for(const k of key){
        if(!node.has(k))
            node.set(k, new Map());
        node = node.get(k);
    }
    node.set("#", val);
};

/** 
 * @param {string} prefix
 * @return {number}
 */
MapSum.prototype.sum = function(prefix) {
    let node = this.root;
    for(const k of prefix){
        if(!node.has(k))
            return 0;
        node = node.get(k);
    }
    return this.dfs(node);
};

MapSum.prototype.dfs = function(node) {
    let ans = 0;
    for(const k of node.keys()){
        if(k == "#")
            ans += node.get(k);
        else
            ans += this.dfs(node.get(k));
    }
    return ans;
};

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */
```
```Go []
type TrieNode struct{
    m map[rune]*TrieNode
    val int
}

type MapSum struct {
    root *TrieNode
}

func Constructor() MapSum {
    return MapSum{root: &TrieNode{m: map[rune]*TrieNode{}}}
}


func (this *MapSum) Insert(key string, val int)  {
    node := this.root
    for _, r := range key {
        _, ok := node.m[r]
        if !ok {
            node.m[r] = &TrieNode{m: map[rune]*TrieNode{}}
        }
        node = node.m[r]
    }
    node.val = val
    return
}


func (this *MapSum) Sum(prefix string) int {
    node := this.root
    for _, r := range prefix {
        _, ok := node.m[r]
        if !ok {
            return 0
        }
        node = node.m[r]
    }
    return node.Dfs()
}

func (this *TrieNode) Dfs() int {
    ans := this.val
    for _,v := range this.m {
        ans += v.Dfs()
    }
    return ans
}

/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
```
BFS
```Python3 []
class MapSum:

    def __init__(self):
        self.trie = dict()

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for k in key:
            if k not in node:
                node[k] = dict()
            node = node[k]
        node["#"] = val

    def sum(self, prefix: str) -> int:
        node = self.trie
        for k in prefix:
            if k not in node:
                return 0
            node = node[k]
        queue = deque([node])
        ans = 0
        while queue:
            node = queue.popleft()
            for k,v in node.items():
                if k == "#":
                    ans += v
                else:
                    queue.append(v)
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```
```Go []
type TrieNode struct{
    m map[rune]*TrieNode
    val int
}

type MapSum struct {
    root *TrieNode
}

func Constructor() MapSum {
    return MapSum{root: &TrieNode{m: map[rune]*TrieNode{}}}
}


func (this *MapSum) Insert(key string, val int)  {
    node := this.root
    for _, r := range key {
        _, ok := node.m[r]
        if !ok {
            node.m[r] = &TrieNode{m: map[rune]*TrieNode{}}
        }
        node = node.m[r]
    }
    node.val = val
    return
}


func (this *MapSum) Sum(prefix string) int {
    node := this.root
    for _, r := range prefix {
        _, ok := node.m[r]
        if !ok {
            return 0
        }
        node = node.m[r]
    }
    queue := make([]*TrieNode, 1)
    queue[0] = node
    ans := 0
    for len(queue) > 0 {
        node = queue[0]
        queue = queue[1:]
        ans += node.val
        for _, r := range node.m{
            queue = append(queue, r)
        }
    }
    return ans
}

/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
```